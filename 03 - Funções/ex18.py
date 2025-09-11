def calcular(operador):
    if operador == "+":
        return lambda a,b: a + b
    elif operador == "-":
        return lambda a,b: a - b
    else:
        return lambda a,b: "Operador inválido"

# Teste
soma = calcular("+")
subtracao = calcular("-")
invalido = calcular("*")

print(f"Soma: {soma(5,5)}")
print(f"Subtração: {subtracao(10,5)}")
print(invalido(2,3))