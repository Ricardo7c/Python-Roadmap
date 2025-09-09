num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print("O maior número é:", maior)