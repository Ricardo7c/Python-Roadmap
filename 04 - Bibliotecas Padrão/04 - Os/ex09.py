import os

caminho = input("Digite o caminho: ")

arquivo = os.path.basename(caminho)

print(f"Nome do arquivo: {arquivo}")