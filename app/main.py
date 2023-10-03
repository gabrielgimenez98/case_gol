from flask import Flask, request, jsonify, Response
import redis
from services.chart import create_chart

from services.csv import extract_csv_data
from services.sql import insert_into_sql, filter_by_date, filter_by_market, filter_for_chart

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/")
def index():
	return 'Health ok'

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Verifique se o usuário já existe no Redis
        if r.get(username):
            return jsonify({'message': 'Usuário já existe'}), 400

        # Armazene o usuário e a senha no Redis
        r.set(username, password)

        return jsonify({'message': 'Usuário cadastrado com sucesso'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def _login(username="", password=""):
    try:

        # Verifique se o usuário existe no Redis
        stored_password = r.get(username)

        if stored_password is None:
            raise Exception("Usuário não encontrado")

        if password == stored_password.decode('utf-8'):
            return
        else:
            raise Exception("Erro no login, Senha incorreta")

    except Exception as e:
        raise e

@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()
        username = data.get('username',"")
        password = data.get('password',"")
        _login(username,password)
        data = extract_csv_data()
        insert_into_sql(data=data)
        
        return jsonify({'message': 'Dados Inseridos com sucesso'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/filter_data_by_date', methods=['POST'])
def filter_data_by_date():
    try:
        data = request.get_json()
        month = data.get('month')
        year = data.get('year')
        username = data.get('username',"")
        password = data.get('password',"")
        _login(username,password)
        
        if not (month or year):
            return jsonify({'message': 'Envie mes ou ano para fazer filtro'}), 400
        
        results = filter_by_date(table_name="voos", year=year, month=month)
        
        return jsonify({'results': results}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/filter_data_by_market', methods=['POST'])
def filter_data_by_market():
    try:
        data = request.get_json()
        market = data.get('market')
        username = data.get('username',"")
        password = data.get('password',"")
        _login(username,password)
        
        if not market:
            return jsonify({'message': 'Envie mercado para fazer filtro'}), 400
        
        results = filter_by_market(table_name="voos", market=market)
        
        return jsonify({'results': results}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/chart', methods=['POST'])
def chart():
    try:
        data = request.get_json()
        username = data.get('username',"")
        password = data.get('password',"")
        _login(username,password)
        market = data.get('market')
        initial_month = data.get('initial_month')
        initial_year = data.get('initial_year')
        end_month= data.get('end_month')
        end_year= data.get('end_year')
        x,y = filter_for_chart(table_name="voos",initial_year=initial_year, initial_month=initial_month,end_year=end_year, end_month=end_month, market=market)
        chart_draw = create_chart(x, y)
        return Response(chart_draw, content_type='image/png')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == "__main__":
	app.run()