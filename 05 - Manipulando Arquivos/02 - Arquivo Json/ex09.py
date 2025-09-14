import json

with open('produtos.json', 'r', encoding='utf-8') as arquivo:
    produtos = json.load(arquivo)

for cada in produtos:
    if cada['preco'] > 500:
        print(f"Produdo: {cada["nome"]} | Preco: {cada["preco"]}")

