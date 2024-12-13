def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Inpar"
    

num1 = 5
num2 = 8
num3 = 33

print(f"{num1} é {verificar_paridade(num1)}")
print(f"{num2} é {verificar_paridade(num2)}")
print(f"{num3} é {verificar_paridade(num3)}")