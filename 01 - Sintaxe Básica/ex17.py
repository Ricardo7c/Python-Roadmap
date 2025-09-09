frase = input("Digite uma frase: ")
frase = frase.lower()
vogais = "aeiou"
contador = 0

for char in frase:
    if char in vogais:
        contador += 1

print("A frase tem", contador, "vogais.")