lista = list(range(1, 7))

# Usando filter e lambda para obter apenas os números pares
pares = list(filter(lambda x: x % 2 == 0, lista))


print(pares)