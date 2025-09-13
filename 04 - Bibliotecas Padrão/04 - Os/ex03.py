import os

pasta = input("Digite o nome da pasta: ")

os.mkdir(pasta)
print(f"Pasta {pasta} criada com sucesso!")