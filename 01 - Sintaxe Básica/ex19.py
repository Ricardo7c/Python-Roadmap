frase = input("Digite uma frase sem acentos: ").lower()
vogais = consoantes = 0
for letra in frase:
    if letra.isalpha():
        if letra in "aeiouáéíóúãõâêîôû":
            vogais += 1
        else:
            consoantes += 1

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")