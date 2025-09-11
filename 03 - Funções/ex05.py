def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Inpar"
    

num1 = 4
num2 = 7

print(f"Número {num1} é {verificar_paridade(num1)}")
print(f"Número {num2} é {verificar_paridade(num2)}")