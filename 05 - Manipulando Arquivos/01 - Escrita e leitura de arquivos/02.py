nova_linha = input("Digite a linha para adicionar: ")

nome_arquivo = 'texto.txt'

with open(nome_arquivo, 'a') as arquivo:
    arquivo.write(nova_linha+ '\n')
    print(f"Linha adicionada a '{nome_arquivo}'")