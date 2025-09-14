with open('origem.txt', 'r') as origem:
    conteudo = origem.read()

with open('copia.txt', 'w') as copia:
    print("Arquivo 'origem.txt' copiado para 'copia.txt'")
    copia.write(conteudo)