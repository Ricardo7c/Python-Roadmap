import csv

nomes = []

with open('alunos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        nomes.append(linha[0])

print(nomes)