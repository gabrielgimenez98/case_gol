from flask import Flask, request, jsonify
import redis
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/")
def index():
	return 'Olá Mundo!!!'

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
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

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Verifique se o usuário existe no Redis
        stored_password = r.get(username)

        if stored_password is None:
            return jsonify({'message': 'Usuário não encontrado'}), 404

        if password == stored_password.decode('utf-8'):
            return jsonify({'message': 'Login bem-sucedido'}), 200
        else:
            return jsonify({'message': 'Senha incorreta'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
	app.run()