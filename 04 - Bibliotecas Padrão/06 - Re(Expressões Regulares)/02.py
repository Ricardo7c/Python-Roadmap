import re

frase = input("Digite uma frase: ")

if re.search("Python", frase, re.IGNORECASE):
    print("A palavra 'Python' foi encontrada")
else:
    print("A palavra 'Python' não foi encontrada")