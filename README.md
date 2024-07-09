# Projeto: Compilação e Transformação de Dados dos Maiores Bancos do Mundo

## Objetivo do Projeto

Este projeto visa desenvolver um sistema automatizado para compilar uma lista dos 10 maiores bancos do mundo, classificados por capitalização de mercado em bilhões de dólares. Além disso, os dados devem ser convertidos e armazenados em diferentes moedas (GBP, EUR e INR) com base em informações de taxa de câmbio fornecidas em um arquivo CSV. O objetivo é preparar esses dados trimestralmente e salvar os resultados em formatos CSV e em uma tabela de banco de dados.

## Cenário

Você foi contratado como engenheiro de dados por uma organização de pesquisa. Seu chefe solicitou a criação de um código que possa ser utilizado para gerar relatórios trimestrais, processando e transformando os dados financeiros dos maiores bancos do mundo.

## Detalhes do Código

| Parâmetro                              | Valor                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------|
| Nome do arquivo                        | `banks_project.py`                                                             |
| URL de dados                           | `https://en.wikipedia.org/wiki/List_of_largest_banks`                          |
| Caminho CSV da taxa de câmbio          | `./exchange_rate.csv`                                                          |
| Atributos da tabela (somente extração) | `Name`, `MC_USD_Billion`                                                       |
| Atributos da tabela final              | `Name`, `MC_USD_Billion`, `MC_GBP_Billion`, `MC_EUR_Billion`, `MC_INR_Billion` |
| Caminho CSV de saída                   | `./Largest_banks_data.csv`                                                     |
| Nome do banco de dados                 | `Banks.db`                                                                     |
| Nome da tabela                         | `Largest_banks`                                                                |
| Arquivo de log                         | `code_log.txt`                                                                 |

## Tarefas

1. **Função de Log**
    - Escreva uma função `log_progress()` para registrar o progresso do código em diferentes estágios em um arquivo `code_log.txt`.

2. **Extração de Dados**
    - Extraia as informações tabulares da URL fornecida sob o título `By market capitalization` e salve em um dataframe.
    - Escreva o código para uma função `extract()` para executar a extração de dados necessárias.
    - Execute uma chamada de função para `extract()` e verifique a saída.

3. **Transformação de Dados**
    - Transforme o dataframe adicionando colunas para `MC_GBP_Billion`, `MC_EUR_Billion` e `MC_INR_Billion`, arredondadas para 2 casas decimais, com base nas informações de taxa de câmbio compartilhadas como um arquivo CSV.
    - Escreva o código para uma função `transform()` para executar a tarefa mencionada.
    - Execute uma chamada de função `transform()` e verifique a saída.

4. **Carregamento para CSV**
    - Carregue o dataframe transformado em um arquivo CSV de saída.
    - Escreva uma função `load_to_csv()`, execute uma chamada de função e verifique a saída.

5. **Carregamento para Banco de Dados**
    - Carregue o dataframe transformado em um servidor de banco de dados SQL como uma tabela.
    - Escreva uma função `load_to_db()`, execute uma chamada de função e verifique a saída.

6. **Consultas no Banco de Dados**
    - Execute consultas na tabela do banco de dados.
    - Escreva uma função `query_db()`, execute um conjunto de consultas e verifique a saída.

7. **Verificação de Logs**
    - Verifique se as entradas de log foram concluídas em todos os estágios, verificando o conteúdo do arquivo `code_log.txt`.

## Bibliotecas Necessárias

As seguintes bibliotecas foram usadas para implementar o projeto:

1. `requests` - Biblioteca usada para acessar as informações da URL.
2. `bs4` - Biblioteca que contém a função BeautifulSoup usada para webscraping.
3. `pandas` - Biblioteca usada para processar os dados extraídos, armazená-los nos formatos necessários e se comunicar com os bancos de dados.
4. `sqlite3` - Biblioteca necessária para criar uma conexão com o servidor de banco de dados.
5. `numpy` - Biblioteca necessária para operações matemáticas, como arredondamento.
6. `datetime` - Biblioteca que contém a função datetime usada para extrair o registro de data e hora para fins de registro.

Embora `requests`, `sqlite3` e `datetime` venham junto com Python, as outras bibliotecas terão que ser instaladas.

### Instalação das Bibliotecas

```bash
python3.11 -m pip install pandas
python3.11 -m pip install numpy
python3.11 -m pip install bs4
```