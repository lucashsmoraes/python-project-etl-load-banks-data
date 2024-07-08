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
                             "MC_USD_Billion": col[2].contents[0].replace('\n', '')}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df


'''
Esta função acessa o arquivo CSV para informações sobre taxas de câmbio e 
adiciona três colunas ao dataframe, cada uma contendo a versão transformada 
da coluna Market Cap para as respectivas moedas.
'''


def transform(df, url):
    dataframe = pd.read_csv(url)
    exchange_rate = dataframe.set_index('Currency')['Rate'].to_dict()
    gdp_list = df["MC_USD_Billion"].tolist()
    gdp_list = [float("".join(x.split(','))) for x in gdp_list]
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in gdp_list]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in gdp_list]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in gdp_list]
    df["MC_USD_Billion"] = gdp_list
    return df


'''
Função responsável por salvar o dataframe final como um arquivo `CSV`
no caminho fornecido. A função não retorna nada.
'''


def load_to_csv(df, csv_path):
    df.to_csv(csv_path)
