import os

caminho = input("Digite o caminho: ")

diretorio = os.path.dirname(caminho)

print(f"Nome do arquivo: {diretorio}")