lista = ["linha1\n", "linha2\n", "linha3\n"]

nome_arquivo = "multilinhas.txt"

with open(nome_arquivo, 'a') as arquivo:
    arquivo.writelines(lista)
    print(f"Arquivo '{nome_arquivo}' criado com 3 linhas.")