with open('multilinhas.txt', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        print(f"{i+1}: {linha.strip()}")