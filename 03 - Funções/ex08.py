lista = [1, 2, 3, 4, 5]
calcular_quadrado = lambda x: x*x


quadrado = map(calcular_quadrado, lista)

print(list(quadrado))