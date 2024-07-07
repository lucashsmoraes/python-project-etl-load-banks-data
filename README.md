# Cenário do Projeto:
Você foi contratado como engenheiro de dados por uma organização de pesquisa. Seu chefe pediu para você criar um código 
que pode ser usado para compilar a lista dos 10 maiores bancos do mundo classificados por capitalização de mercado em bilhões de dólares. 
Além disso, os dados precisam ser transformados e armazenados em `GBP`, `EUR` e `INR` também, de acordo com as informações de taxa de câmbio 
que foram disponibilizadas a você como um arquivo `CSV`. 
A tabela de informações processadas deve ser salva localmente em um formato `CSV` e como uma `tabela` de banco de dados.

Seu trabalho é criar um sistema automatizado para gerar essas informações para que o mesmo possa ser executado em cada trimestre financeiro para preparar o relatório.

Detalhes do código a ser criado abaixo:

| Parâmetro                              | Valor                                                                                             |
|----------------------------------------|---------------------------------------------------------------------------------------------------|
| Nome do arquivo                        | `banks_project.py`                                                                                |
| URL de dados                           | `https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks` |
| Caminho CSV da taxa de câmbio          | `./exchange_rate.csv`                                                                             |
| Atributos da tabela (somente extração) | `Name`, `MC_USD_Billion`                                                                          |
| Atributos da tabela final              | `Name`, `MC_USD_Billion`, `MC_GBP_Billion`, `MC_EUR_Billion`, `MC_INR_Billion`                    |
| Caminho CSV de saída                   | `./Largest_banks_data.csv`                                                                        |
| Nome do banco de dados                 | `Banks.db`                                                                                        |
| Nome da tabela                         | `Largest_banks`                                                                                   |
| Arquivo de log                         | `code_log.txt`                                                                                    |

## Tarefa 1
Escreva uma função ´log_progress()´ para registrar o progresso do código em diferentes estágios em um arquivo `code_log.txt`.

## Tarefa 2
Extraia as informações tabulares da URL fornecida sob o título `By market capitalization` e salve em um dataframe.
1. Inspecione a página da web e identifique a posição e o padrão das informações tabulares no código HTML.
2. Escreva o código para uma função `extract()` para executar a extração de dados necessárias.
3. Execute uma chamada de função para `extract()` verificar a saída.

## Tarefa 3
Transforme o dataframe adicionando colunas para `By market capitalization em GBP, EUR e INR`, arredondadas para 2 casas decimais, 
com base nas informações de taxa de câmbio compartilhadas como um arquivo CSV.
1. Escreva o código para uma função `transform()` executar a tarefa mencionada.
2. Execute uma chamada de função `transform()` e verifique a saída.

## Tarefa 4:
Carregue o dataframe transformado em um arquivo CSV de saída. Escreva uma função `load_to_csv()`, execute uma chamada de função e verifique a saída.

## Tarefa 5:
Carregue o dataframe transformado em um servidor de banco de dados SQL como uma tabela. Escreva uma função `load_to_db()`, execute uma chamada de função e verifique a saída.

## Tarefa 6:
Execute consultas na tabela do banco de dados. Escreva uma função `load_to_db()`, execute um conjunto dado de consultas e verifique a saída.

## Tarefa 7:
Verifique se as entradas de log foram concluídas em todos os estágios, verificando o conteúdo do arquivo `code_log.txt`.
