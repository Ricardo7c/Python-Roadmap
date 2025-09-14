import json

with open('produtos.json', 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)


for cada in conteudo:
    print(f"Produto: {cada['nome']} | Preço: {cada['preco']}")