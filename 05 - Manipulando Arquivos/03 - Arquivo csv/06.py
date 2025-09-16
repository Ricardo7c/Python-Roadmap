import csv

total = 0

with open('produtos.csv', 'r') as arquivo:
    conteudo = csv.reader(arquivo)
    next(conteudo)

    for cada in conteudo:
        total += float(cada[1])*int(cada[2])

    print(f'Valor total do estoque: R$ {total:.2f}')