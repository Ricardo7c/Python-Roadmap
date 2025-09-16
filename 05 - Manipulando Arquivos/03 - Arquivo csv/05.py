import csv

produtos = [
    {'produto': 'Maçã', 'preço': 2.50, 'quantidade': 100},
    {'produto': 'Banana', 'preço': 1.75, 'quantidade': 150},
    {'produto': 'Laranja', 'preço': 3.00, 'quantidade': 120}
]

# Transforma as chaves do primeiro dicinario no cabeçalho
cabecalho = list(produtos[0].keys())

with open('produtos.csv', 'w', newline='') as arquivo:

    conteudo = csv.DictWriter(arquivo, fieldnames=cabecalho)
    conteudo.writeheader()
    conteudo.writerows(produtos)
    
print("Arquivo 'produtos.csv' criado com 3 produtos.")
