import re

frase = input("Digite uma frase: ")
partes = re.split(r'\s+', frase)

print(partes)