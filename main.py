from banks_project import extract, transform, load_to_csv, load_to_db, run_query, log_progress
import sqlite3

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
csv_path = './exchange_rate.csv'
table_attribs = ["Name", "MC_USD_Billion"]
table_attribs_final = ['Name', "MC_USD_Billion", 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']
output_path = './Largest_banks_data.csv'
table_name = 'Largest_banks'

if __name__ == '__main__':
    log_progress('Iniciando processo ETL')
    df = extract(url, table_attribs)
    print(df)

    log_progress('Extração de dados concluída. Iniciando o processo de transformação')
    df2 = transform(df, csv_path)
    print(df2['MC_EUR_Billion'][5])

    log_progress('Transformação de dados concluída. Iniciando processo de carregamento')
    load_to_csv(df2, output_path)

    log_progress('Dados salvos em arquivo CSV. Iniciando conecção com banco de dados')
    sql_connection = sqlite3.connect('Banks.db')

    log_progress('Conecção SQL Finalizada, Iniciando carregamento dado como tabela no banco de dados')
    load_to_db(df, sql_connection, table_name)

    log_progress('Dados carregados com sucesso. Iniciando consulta na tabela')
    query_statement = f"SELECT * FROM Largest_banks"
    run_query(query_statement, sql_connection)

    log_progress('Iniciando consulta capitalização média de todos os bancos em bilhões de dólares')
    query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
    run_query(query_statement, sql_connection)

    log_progress('Iniciando consulta de nomes dos 5 principais bancos')
    query_statement = f"SELECT Name from {table_name} LIMIT 5"
    run_query(query_statement, sql_connection)

    log_progress('Processo finalizado com sucesso')
    sql_connection.close()
