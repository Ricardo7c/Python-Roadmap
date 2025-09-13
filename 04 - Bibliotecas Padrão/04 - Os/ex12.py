import os

arquivo = input("Digite o arquivo: ")

nome, extensao = os.path.splitext(arquivo)

print(f"Nome: {nome}")
print(f"Extensão: {extensao}")