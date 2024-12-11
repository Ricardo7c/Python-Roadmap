frase = input("Digite uma frase: ")
palavra = input("Digite a palavra que deseja substituir: ")
substituta = input("Digite a nova palavra: ")

nova_frase = frase.replace(palavra, substituta)

print(f"Frase atualizada: {nova_frase}")