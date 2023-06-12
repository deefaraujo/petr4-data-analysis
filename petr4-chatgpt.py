# Importando as bibliotecas necessárias
import yfinance as yf
import pandas as pd
import sqlite3

# PERGUNTA AO CHATGPT
# Utilizando a linguagem Python, crie uma função que seja capaz de utilizar a API do Yahoo Finance para baixar os dados históricos diários das ações da Petrobras (código PETR4). A função deve salvar esses dados em um arquivo .csv.
#
# Por favor, inclua comentários no código para explicar o que cada parte da função faz. Além disso, forneça instruções sobre como executar a função e quaisquer dependências de biblioteca que possam ser necessárias.
def download_petr4_data():
    # Baixando os dados da Petrobras (PETR4) do Yahoo Finance
    petr4 = yf.Ticker("PETR4.SA")

    # Obtendo os dados históricos diários
    hist = petr4.history(period="max")

    # Salvando os dados em um arquivo .csv
    hist.to_csv('petr4_data.csv')

# PERGUNTA AO CHATGPT
# Desenvolva uma função em Python que receba um nome de arquivo .csv como entrada. Esta função deve carregar o conteúdo do arquivo e retornar um dataframe do pandas com os dados do arquivo.
# Depois de criar a função, use-a para carregar o arquivo .csv que contém os dados históricos diários das ações da Petrobras (código PETR4) que foi baixado da API do Yahoo Finance na função anterior. Imprima as últimas 10 linhas do dataframe.
#
# Por favor, inclua comentários no código para explicar o que cada parte da função faz. Além disso, forneça instruções sobre como executar a função e quaisquer dependências de biblioteca que possam ser necessárias.
def load_csv_to_dataframe(filename):
    # Carregando o arquivo .csv em um dataframe do pandas
    df = pd.read_csv(filename)

    # Retornando o dataframe
    return df
# PERGUNTA AO CHATGPT
# Desenvolva uma função em Python que receba como entrada um dataframe do pandas e o nome de uma de suas colunas. Esta função deve calcular e retornar a média e o desvio padrão dos valores contidos na coluna especificada.
#
# Por favor, inclua comentários no código para explicar o que cada parte da função faz. Além disso, forneça instruções sobre como executar a função e quaisquer dependências de biblioteca que possam ser necessárias.
def calculate_mean_std(df, column_name):
    # Calculando a média dos valores na coluna especificada
    mean = df[column_name].mean()

    # Calculando o desvio padrão dos valores na coluna especificada
    std = df[column_name].std()

    # Retornando a média e o desvio padrão
    return mean, std
# PERGUNTA AO CHATGPT
# Desenvolva uma função em Python que receba como entrada um dataframe do pandas, onde cada coluna contém uma série de números, e o nome de uma dessas colunas. A função deve retornar um novo dataframe que é o resultado da ordenação das linhas do dataframe de entrada em ordem crescente com base nos valores da coluna especificada.
#
# Por favor, inclua comentários no código para explicar o que cada parte da função faz. Além disso, forneça instruções sobre como executar a função e quaisquer dependências de biblioteca que possam ser necessárias.
def sort_dataframe(df, column_name):
    # Ordenando o dataframe em ordem crescente com base nos valores da coluna especificada
    sorted_df = df.sort_values(by=column_name)

    # Retornando o dataframe ordenado
    return sorted_df
# PERGUNTA AO CHATGPT
# Desenvolva uma função em Python que receba como entrada o nome de um arquivo .csv. A função deve carregar os dados do arquivo e, utilizando a biblioteca sqlite3, criar um banco de dados SQLite com um nome padrão. Em seguida, a função deve criar uma tabela nesse banco de dados que contém os dados do arquivo .csv, mantendo os nomos das colunas do arquivo original. Por fim, a função deve salvar o banco de dados em um arquivo de saída.

# Por favor, inclua comentários no código para explicar o que cada parte da função faz. Além disso, forneça instruções sobre como executar a função e quaisquer dependências de biblioteca que possam ser necessárias.
def csv_to_sqlite(filename):
    # Carregando o arquivo .csv em um dataframe do pandas
    df = pd.read_csv(filename)

    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('my_database.db')

    # Criando uma tabela no banco de dados SQLite com os dados do dataframe
    # O nome da tabela será 'my_table'
    df.to_sql('my_table', conn, if_exists='replace', index=False)

    # Fechando a conexão com o banco de dados SQLite
    conn.close()

# Executando as funções
download_petr4_data()
df = load_csv_to_dataframe('petr4_data.csv')
mean, std = calculate_mean_std(df, 'Close')
sorted_df = sort_dataframe(df, 'Close')
csv_to_sqlite('petr4_data.csv')
