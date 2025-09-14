import json

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)


conteudo ['Idade'] = 26


with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)