from datetime import datetime

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