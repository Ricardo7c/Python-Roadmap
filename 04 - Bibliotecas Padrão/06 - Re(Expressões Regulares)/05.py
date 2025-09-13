import re

frase = input("Digite uma frase: ")
palavras = re.split(r'\s+', frase)

print(f"Lista de palavras: {palavras}")