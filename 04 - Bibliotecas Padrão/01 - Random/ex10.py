from random import gauss

gerados = []

for _ in range(5):
    gerados.append(round(gauss(50, 10), 2))

print(f"Valores gerados: {gerados}")