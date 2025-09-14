with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()

novo_conteudo = conteudo.replace("foo", "bar")

with open('dados.txt', 'w') as arquivo:
    arquivo.write(novo_conteudo)
    print("Arquivo atualizado com sucesso.")