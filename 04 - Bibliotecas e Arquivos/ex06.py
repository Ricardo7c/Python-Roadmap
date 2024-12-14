import json;


dados = {"nome": "Ricardo", "idade": 34}
caminho = "04 - Bibliotecas e Arquivos/arquivo.json"

# Cria um arquivo.json e escreve os dados do dicionario no formato json
with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
