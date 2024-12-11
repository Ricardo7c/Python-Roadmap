n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

if n1 >= n2 and n1 > n3:
    maior = n1
elif n2 >= n1 and n2 > n3:
    maior = n2
elif n3 >= n1 and n3 > n2:
    maior = n3

print(f"O maior numero é {maior}")