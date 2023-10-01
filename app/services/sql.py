import sqlite3
import mysql.connector



def inserir_dados_sql(dados, nome_banco, nome_tabela):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'biel0104',
        "database":'gol'
        }
        # Conectar ao banco de dados
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        for item in dados:
            try:
                consulta = "INSERT INTO voos (ano, mes, mercado, rpk) VALUES (%s, %s, %s, %s)"
                valores = (item['ano'], item['mes'], item['mercado'], item['rpk'])
                cursor.execute(consulta, valores)
            except:
                continue

            cursor.execute(consulta, tuple(item.values()))

        conexao.commit()

        conexao.close()


    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados no SQLite: {erro}")
        raise erro
    
def filtrar_dados_sql(nome_banco, nome_tabela, campo, valor):
    try:
        # Conectar ao banco de dados
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'biel0104',
        "database":'gol'
        }
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        consulta_sql = f"SELECT * FROM {nome_tabela} WHERE {campo} = %s"
        cursor.execute(consulta_sql, (valor,))

        resultados = []
        for row in cursor.fetchall():
            row_dict = {}
            for idx, col in enumerate(cursor.description):
                col_name = col[0]
                col_value = row[idx]
                row_dict[col_name] = col_value
            resultados.append(row_dict)

        conexao.close()
        
        return resultados
    
    except sqlite3.Error as erro:
        print(f"Erro ao filtrar dados no SQLite: {erro}")
        raise erro