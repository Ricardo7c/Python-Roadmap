import os

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def numero(texto):
    while True:
        n = input(texto)
        try:
            return float(n)
        except ValueError:
            print("Valor inválido!")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def opcoes():
    while True:
        print("Escolha a operação: ")
        print("A. Adição")
        print("B. Subtração")
        print("C. Multiplicação")
        print("D. Divisão")
        print("E. Sair")
        op = input("Digire uma das opções: ").upper()
        if op in "ABCDE":
            limpar_terminal()
            break
        else:
            limpar_terminal()
            print("Opção invalida!")
    return op


while True:
    op = opcoes()
    if op == "A":
        print("====== Adição ======")
    elif op == "B":
        print("====== Subtração ======")
    elif op == "C":
        print("====== Multiplicação ======")
    elif op == "D":
        print("====== Divisão ======")
    else:
        print("Programa encerrado!")
        break


    n1 = numero("Digite o primeiro numero: ")
    while True:
        n2 = numero("Digite o segundo numero: ")
        if n2 == 0 and op == "D":
            print("Não é permitido dividir por Zero, digite um numero valido!")
        else:
            break

    if op == "A":
        print(f"{n1} + {n2} = {soma(n1, n2)}")
    elif op == "B":
        print(f"{n1} - {n2} = {sub(n1, n2)}")
    elif op == "C":
        print(f"{n1} * {n2} = {multi(n1, n2)}")
    elif op == "D":
        print(f"{n1} / {n2} = {div(n1, n2)}")
    
    print("=============================")




