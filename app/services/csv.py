import csv
import pandas as pd

def extract_csv_data():
    data = []
    with open('app/services/Dados_Estatisticos.csv', newline='', encoding='utf-8') as file:

        df = pd.read_csv(file, encoding='ISO-8859-1', sep=';')

        for index, row in df.iterrows():
            try:
                if filter_data(index):
                    data.append(mount_item(item=index))
            except:
                continue

    return data


def filter_data(item):
    return item[0] == "GLO" and item[18] == "REGULAR" and item[17] == "DOMÉSTICA"

def mount_item(item):
    return {
        "ano": item[3],
        "mes": item[4],
        "mercado": mount_market(item[5],item[11]),
        "rpk": item[25]
    }
def mount_market(origin,destination):
    return origin + destination if origin < destination else destination + origin