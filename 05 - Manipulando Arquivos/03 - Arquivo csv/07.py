import csv 

with open('produtos.csv', 'r') as arquivo:
    conteudo = csv.reader(arquivo)
    next(conteudo)

    for cada in conteudo:
        if float(cada[1]) > 2:
            print(f"Produto: {cada[0]} | Preço: R$ {float(cada[1]):.2f} | Quantidade: {cada[2]}")