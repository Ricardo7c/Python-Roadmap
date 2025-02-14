def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    # Função que será retornada caso a operação seja inválida
    def invalido(*args):
        return "Operacao invalida"
    
    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    else:
        return invalido
    

resultado = calcular("-")(10, 5)
print(resultado)