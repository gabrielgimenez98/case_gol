import csv
import pandas as pd

def filtra_linha_csv():
    lista_itens = []
    with open('app/services/Dados_Estatisticos.csv', newline='', encoding='utf-8') as file:

        df = pd.read_csv(file, encoding='ISO-8859-1', sep=';')

        for index, row in df.iterrows():
            try:
                lista_itens.append(monta_item_filtrado(item=index))
            except:
                continue

    return lista_itens

# def ler_csv():
#     # df = pd.read_csv('app/services/Dados_Estatisticos.csv', on_bad_lines='skip',header=0)
#     with open('app/services/Dados_Estatisticos.csv', newline='', encoding='utf-8') as file:

#         df = pd.read_csv(file, encoding='ISO-8859-1', sep=';')

#         for index, row in df.iterrows():
#             lista_itens.append(monta_item_filtrado(item=item))
    
#     return None

    #     reader = csv.reader(file)
    #     column_names = next(reader)  # Reads the first line, which contains the header
    #     data = {col: [] for col in column_names}
    #     for row in reader:
    #         for key, value in zip(column_names, row):
    #             data[key].append(value)

    #     import pdb;pdb.set_trace()

def filtra_dados(item):
    return item[0] == "GLO" and item[18] == "REGULAR" and item[17] == "DOMÉSTICA"

def monta_item_filtrado(item):
    return {
        "ano": item[3],
        "mes": item[4],
        "mercado": monta_mercado(item[5],item[11]),
        "rpk": item[25]
    }
def monta_mercado(origem,destino):
    return origem + destino if origem < destino else destino + origem