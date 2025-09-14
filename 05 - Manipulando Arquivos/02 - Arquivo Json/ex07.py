import json

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)

telefone = conteudo.get('telefone', 'telefone não informado')


print(telefone)