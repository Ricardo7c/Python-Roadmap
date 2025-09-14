import json

with open('clientes1.json', 'r', encoding='utf-8') as arquivo1:
    clientes1 = json.load(arquivo1)

with open('clientes2.json', 'r', encoding='utf-8') as arquivo2:
    clientes2 = json.load(arquivo2)


clientes = clientes1+clientes2


with open('clientes.json', 'w', encoding='utf-8') as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
    print("Clientes mesclados em 'clientes.json'")