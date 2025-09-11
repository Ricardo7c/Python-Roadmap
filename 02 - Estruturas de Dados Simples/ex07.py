numeros = []

for i in range(7):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numeros.sort()
print("Lista em ordem crescente:", numeros)

numeros.reverse()
print("Lista invertida:", numeros)