n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = n1+n2
sub = n1-n2
mult = n1*n2

print(f"Soma: {n1+n2}")
print(f"Subtração: {n1-n2}")
print(f"Multiplicação: {n1*n2}")

if n2 == 0:
    print("Não é possivel dividir por zero")
else:
    print(f"Divisão: {n1/n2:.2f}")