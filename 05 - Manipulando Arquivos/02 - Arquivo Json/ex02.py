import json

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    info = json.load(arquivo)

for cada in info.items():
    print(f"{cada[0]}: {cada[1]}")
