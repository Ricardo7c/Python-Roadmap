import os

arquivo = input("Digite o caminho: ")

if os.path.exists(arquivo):
    print("O caminho existe!")
else:
    print("O caminho não existe")