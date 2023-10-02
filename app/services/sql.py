import sqlite3
import mysql.connector



def inserir_dados_sql(dados, nome_banco, nome_tabela):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
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
    
def filtrar_dados_sql_data(nome_banco, nome_tabela, ano, mes):
    try:
        # Conectar ao banco de dados
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        consulta_sql = f"""
                        SELECT *
                        FROM {nome_tabela}
                        WHERE
                            (ano = %s OR %s IS NULL)
                            AND (mes = %s OR %s IS NULL);
                    """
        cursor.execute(consulta_sql,(ano, ano, mes, mes))

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
    
def filtrar_dados_sql_mercado(nome_banco, nome_tabela, mercado):
    try:
        # Conectar ao banco de dados
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        consulta_sql = f"""
                        SELECT *
                        FROM {nome_tabela}
                        WHERE
                            mercado = %s
                            ;
                    """
        cursor.execute(consulta_sql,(mercado,))

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
    

def filtrar_dados_sql_grafico(nome_banco, nome_tabela, mercado, ano_inicio,ano_fim, mes_inicio, mes_fim):
    try:
        # Conectar ao banco de dados
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        consulta_sql = f"""
                        SELECT CONCAT(ano, '-', mes) AS ano_mes, rpk
                        FROM {nome_tabela}
                        WHERE
                            mercado = %s
                            AND CONCAT(ano, '-', mes) BETWEEN %s AND %s
                            ;
                    """
        cursor.execute(consulta_sql,(mercado,f"{ano_inicio}-{mes_inicio}", f"{ano_fim}-{mes_fim}"))

        resultados = cursor.fetchall()

        # Separar os resultados em listas separadas para x e y
        x = [resultado[0] for resultado in resultados]
        y = [resultado[1] for resultado in resultados]


        conexao.close()
        
        return x,y
    
    except sqlite3.Error as erro:
        print(f"Erro ao filtrar dados no SQLite: {erro}")
        raise erro