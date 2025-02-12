lista = [1, 2, 3, 4, 5, 6]
div_por3 = lambda x: x % 3 == 0


quadrado = filter(div_por3, lista)

print(list(quadrado))