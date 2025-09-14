import json

info = {"Nome":"Ana", "Idade":"30", "Cidade": "São Paulo"}

with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(info, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo 'pessoa.json' criado com sucesso." )