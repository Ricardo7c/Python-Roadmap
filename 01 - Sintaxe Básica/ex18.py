def inverter_frase(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = " ".join(palavras_invertidas)
    return frase_invertida

frase = input("Digite uma frase: ")
frase_invertida = inverter_frase(frase)
print("Frase invertida:", frase_invertida)