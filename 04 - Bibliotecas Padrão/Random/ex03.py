from random import uniform

min = float(input("Digite o valor mínimo: "))
max = float(input("Digite o valor máximo: "))

print(f"O Número sorteado: {uniform(min, max):.2f}")