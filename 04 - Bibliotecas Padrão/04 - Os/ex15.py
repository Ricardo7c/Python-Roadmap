from genericpath import isfile
import os

caminho = input("Digite o caminho: ")

if os.path.isdir(caminho):
    print("É um diretório!")
else:
    print("Não é um diretório!")