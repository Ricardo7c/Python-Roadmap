import os;

caminho = "04 - Bibliotecas e Arquivos"

os.mkdir(f"{caminho}/novo_diretorio")

for cada in os.listdir(caminho):
    print(cada)

os.rmdir(f"{caminho}/novo_diretorio")

