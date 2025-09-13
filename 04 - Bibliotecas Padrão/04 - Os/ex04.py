import os

pasta = input("Digite o nome da pasta para remover: ")

os.rmdir(pasta)
print(f"Pasta {pasta} removida com sucesso!")