msg = input("Digite uma menssagem: ")

nome_arquivo = "texto.txt"

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(msg)
    print(f"Mensagem salva em {nome_arquivo}")