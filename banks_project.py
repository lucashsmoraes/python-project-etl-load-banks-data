from datetime import datetime
from bs4 import BeautifulSoup
import requests as req
import pandas as pd

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
                data_dict = {"Bank name": col[1].find_all('a')[1].contents[0],
                             "Market cap": col[2].contents[0].replace('\n', '')}
                print(data_dict)
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df
