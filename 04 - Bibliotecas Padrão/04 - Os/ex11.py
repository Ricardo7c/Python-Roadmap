import os

caminho = input("Digite o caminho: ")

separado = os.path.split(caminho)

print(f"Separação: {separado}")