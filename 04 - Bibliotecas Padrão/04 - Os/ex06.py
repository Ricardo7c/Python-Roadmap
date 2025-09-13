import os

arquivo = input("Digite o nome do arquivo para remover: ")

os.remove(arquivo)

print(f"Arquivo '{arquivo}' removido com sucesso!")