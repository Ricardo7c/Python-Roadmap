import re

frase = input("Digite uma frase: ")

numeros = re.findall(r'\d+', frase)

print(f"Números encontrados: {numeros}")