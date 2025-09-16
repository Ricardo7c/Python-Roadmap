import csv

with open('produtos.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv)
    header = next(reader)
    produtos = []
    for linha in reader:
        produto = dict(zip(header, linha))
        produtos.append(produto)

for produto in produtos:
    print(produto)