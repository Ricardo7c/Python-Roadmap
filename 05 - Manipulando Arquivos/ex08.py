import csv

caminho = "04 - Bibliotecas e Arquivos/arquivo.csv"

# Abrindo o arquivo em modo de leitura
with open(caminho, 'r', newline='', encoding='utf-8') as arquivo:
    # Cria um objeto leitor
    leitor_csv = csv.reader(arquivo)  

    for linha in leitor_csv:
        print(linha) # Cada linha é uma lista
