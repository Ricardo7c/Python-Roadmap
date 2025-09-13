import os

pasta = input("Digite a pasta: ")
arquivo = input("Digite o arquivo: ")

caminho_completo = os.path.join(pasta, arquivo)

print(f"Caminho completo: {caminho_completo}")