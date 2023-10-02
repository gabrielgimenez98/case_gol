import sqlite3
import mysql.connector



def insert_into_sql(data):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        for item in data:
            try:
                sql_query = "INSERT INTO voos (ano, mes, mercado, rpk) VALUES (%s, %s, %s, %s)"
                values = (item['ano'], item['mes'], item['mercado'], item['rpk'])
                cursor.execute(sql_query, values)
            except:
                continue

            cursor.execute(sql_query, tuple(item.values()))

        con.commit()

        con.close()


    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados no SQLite: {erro}")
        raise erro
    
def filter_by_date(table_name, year, month):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        sql_query = f"""
                        SELECT *
                        FROM {table_name}
                        WHERE
                            (ano = %s OR %s IS NULL)
                            AND (mes = %s OR %s IS NULL);
                    """
        cursor.execute(sql_query,(year, year, month, month))

        results = []
        for row in cursor.fetchall():
            row_dict = {}
            for idx, col in enumerate(cursor.description):
                col_name = col[0]
                col_value = row[idx]
                row_dict[col_name] = col_value
            results.append(row_dict)

        con.close()
        
        return results
    
    except sqlite3.Error as erro:
        print(f"Erro ao filtrar dados no SQLite: {erro}")
        raise erro
    
def filter_by_market(table_name, market):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        sql_query = f"""
                        SELECT *
                        FROM {table_name}
                        WHERE
                            mercado = %s
                            ;
                    """
        cursor.execute(sql_query,(market,))

        results = []
        for row in cursor.fetchall():
            row_dict = {}
            for idx, col in enumerate(cursor.description):
                col_name = col[0]
                col_value = row[idx]
                row_dict[col_name] = col_value
            results.append(row_dict)

        con.close()
        
        return results
    
    except sqlite3.Error as erro:
        print(f"Erro ao filtrar dados no SQLite: {erro}")
        raise erro
    

def filter_for_chart(table_name, market, initial_year,end_year, initial_month, end_month):
    try:
        db_config = {
        "host":'127.0.0.1',
        "user":'root',
        "password":'',
        "database":'gol'
        }
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        query_sql = f"""
                        SELECT CONCAT(ano, '-', mes) AS ano_mes, rpk
                        FROM {table_name}
                        WHERE
                            mercado = %s
                            AND CONCAT(ano, '-', mes) BETWEEN %s AND %s
                            ;
                    """
        cursor.execute(query_sql,(market,f"{initial_year}-{initial_month}", f"{end_year}-{end_month}"))

        resultados = cursor.fetchall()

        # Separar os resultados em listas separadas para x e y
        x = [resultado[0] for resultado in resultados]
        y = [resultado[1] for resultado in resultados]


        con.close()
        
        return x,y
    
    except sqlite3.Error as erro:
        print(f"Erro ao filtrar dados no SQLite: {erro}")
        raise erro