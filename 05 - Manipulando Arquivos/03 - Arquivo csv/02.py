import csv

nome_arquivo = 'alunos.csv'

with open(nome_arquivo, 'r') as arquivo:
    conteudo = csv.reader(arquivo)
    for linha in conteudo:
        print(linha)