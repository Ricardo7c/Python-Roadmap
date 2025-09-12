from random import choices

lista = [1, 2, 4, 9, 11]

sorteio = choices(lista, k=3)

print(f"Números sorteados: {sorteio}")