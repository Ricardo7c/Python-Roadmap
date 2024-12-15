import json;

caminho = "04 - Bibliotecas e Arquivos/arquivo.json"

with open(caminho, "r", encoding="utf-8") as arquivo:
    # Converter o json para dicionario
    dados = json.load(arquivo)


print(dados)