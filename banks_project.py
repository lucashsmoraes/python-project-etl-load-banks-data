from datetime import datetime
from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np

'''
Função responsável por registrar a mensagem logada em um determinado
estágio da execução do código em um arquivo de log. A função não retorna nada
'''


def log_progress(message):
    timestamp_format = '%Y-%n-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./code_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')


'''
 Função responsável por extrair informações necessárias do site e savar
 em um dataframe. A função deverá retornar o dataframe para o processamento
 posterior
'''


def extract(url, table_attribs):
    page = req.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[1].find('a') is not None and '—' not in col[2]:
                data_dict = {"Name": col[1].find_all('a')[1].contents[0],
                             "MC_USD_Billion": float(col[2].contents[0][:-1])}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df


'''
Esta função acessa o arquivo CSV para informações sobre taxas de câmbio e 
adiciona três colunas ao dataframe, cada uma contendo a versão transformada 
da coluna Market Cap para as respectivas moedas.
'''


def transform(df, csv_path):
    dataframe = pd.read_csv(csv_path)
    exchange_rate = dataframe.set_index('Currency')['Rate'].to_dict()
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df["MC_USD_Billion"]]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df["MC_USD_Billion"]]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df["MC_USD_Billion"]]
    return df


'''
Função responsável por salvar o dataframe final como um arquivo `CSV`
no caminho fornecido. A função não retorna nada.
'''


def load_to_csv(df, output_path):
    df.to_csv(output_path)


'''
Função responsável por salvar o dataframe final na tabela do banco de dados
com o nome fornecido. A função não retorna nada
'''


def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)


'''
Função responsável por fazer consulta na tabela do banco de dados e
imprime a saída no terminal. A função não retorna nada
'''


def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql_query(query_statement, sql_connection)
    print(query_output)
