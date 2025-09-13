from genericpath import isfile
import os

caminho = input("Digite o caminho: ")

if os.path.isfile(caminho):
    print("É um arquivo!")
else:
    print("Não é um arquivo!")