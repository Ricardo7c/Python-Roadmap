from random import gauss

gerados = list(round(gauss(50, 10), 2) for _ in range(5))

print(f"Valores gerados: {gerados}")