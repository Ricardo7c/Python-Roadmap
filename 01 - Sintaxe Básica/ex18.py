palavra = input("Digite uma palavra: ").upper()
pl = palavra.replace(" ","")
reverse = pl[::-1]
if pl == reverse:
    print("É um palindromo!")
else:
    print("Não é um palindromo!")