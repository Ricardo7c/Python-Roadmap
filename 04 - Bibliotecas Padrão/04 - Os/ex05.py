import os

arquivo = input("Digite o nome do arquivo/pasta: ")
novo = input("Digite o novo nome: ")

os.rename(arquivo, novo)

print(f"'{arquivo}' foi renomeado para '{novo}'")

