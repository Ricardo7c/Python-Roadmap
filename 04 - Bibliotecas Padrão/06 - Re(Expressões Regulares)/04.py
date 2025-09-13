import re

frase = input("Digite uma frase: ")

modificada = re.sub(r'\bjava\b', 'python' , frase, flags=re.IGNORECASE)

print(modificada)