numeros = (10, 20, 30, 40, 50, 20)
numero = int(input("Digite um número: "))

if numero in numeros:
    print("O índice da primeira ocorrência é:", numeros.index(numero))
else:
    print("Número não encontrado na tupla.")
