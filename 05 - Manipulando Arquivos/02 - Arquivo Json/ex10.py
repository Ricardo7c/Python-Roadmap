import json

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)


json_formatado = json.dumps(conteudo, indent=2, ensure_ascii=False)


print(json_formatado)