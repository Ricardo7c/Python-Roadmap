import json


produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 120},
    {"nome": "Teclado", "preco": 200}
]


with open('produtos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(produtos, arquivo, ensure_ascii=False)
    print("Arquivo 'Produtos.json' criado com 3 produtos")