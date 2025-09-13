import os

arquivo = input("Digire o arquivo: ")

caminho_absoluto = os.path.abspath(arquivo)

print(f"Caminho absoluto: {caminho_absoluto}")