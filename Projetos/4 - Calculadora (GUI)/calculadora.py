import tkinter
from turtle import bgcolor

# Variáveis globais
oper_status = False
oper = ""
num1 = ""

def digitar(valor):
    global oper_status
    if oper_status or visor.get() == "Erro":
        visor.delete(0, tkinter.END)
        oper_status = False
        botoes_op()
    visor.insert(tkinter.END, valor)

def operador(valor, botao):
    global num1, oper, oper_status
    if num1 == "":
        num1 = visor.get()
    else:
        num1 = operacao()
    oper = valor
    oper_status = True
    visor.delete(0, tkinter.END)
    visor.insert(tkinter.END, str(num1))
    destacar_operador(botao) 

def operacao():
    global num1, oper, oper_status
    try:
        n1 = float(num1) if num1 is not None else 0.0
        n2 = float(visor.get())
        if oper == "+":
            return n1 + n2
        elif oper == "-":
            return n1 - n2
        elif oper == "*":
            return n1 * n2
        elif oper == "/":
            return n1 / n2 if n2 != 0 else "Erro"
    except Exception as e:
        oper = ""
        num1 = ""
        return "Erro"

def calcular_resultado():
    global num1, oper, oper_status
    resultado = operacao()
    visor.delete(0, tkinter.END)
    visor.insert(tkinter.END, str(resultado))
    num1 = ""
    oper = ""
    botoes_op()
    resetar_cores_operadores() 
    oper_status = False

def reset():
    global oper, oper_status, num1
    oper_status = False
    oper = ""
    num1 = ""   
    resetar_cores_operadores() 
    visor.delete(0, tkinter.END)

# Desabilita os botões de operação quando a caluladora acusa error
def botoes_op():
    if visor.get() == "Erro":
        eq.config(state="disabled")
        o1.config(state="disabled")
        o2.config(state="disabled")
        o3.config(state="disabled")
        o4.config(state="disabled")
    else:
        eq.config(state="normal")
        o1.config(state="normal")
        o2.config(state="normal")
        o3.config(state="normal")
        o4.config(state="normal")

# Configuração da janela
janela = tkinter.Tk()
janela.geometry("308x338")
janela.title("Calculadora")

# Visor
visor = tkinter.Entry(janela, font=("Arial", 30), bg="lightgray", width=9)
visor.grid(row=0, column=0, columnspan=3, sticky="ew")

# Botões
cl = tkinter.Button(janela, text="cls", font=("Arial", 18, "bold"), width=4, height=1, command=reset)
n1 = tkinter.Button(janela, text="1", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("1"))
n2 = tkinter.Button(janela, text="2", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("2"))
n3 = tkinter.Button(janela, text="3", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("3"))
o1 = tkinter.Button(janela, text="+", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: operador("+", o1))
n4 = tkinter.Button(janela, text="4", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("4"))
n5 = tkinter.Button(janela, text="5", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("5"))
n6 = tkinter.Button(janela, text="6", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("6"))
o2 = tkinter.Button(janela, text="-", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: operador("-", o2))
n7 = tkinter.Button(janela, text="7", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("7"))
n8 = tkinter.Button(janela, text="8", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("8"))
n9 = tkinter.Button(janela, text="9", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("9"))
o3 = tkinter.Button(janela, text="*", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: operador("*", o3))
ponto = tkinter.Button(janela, text=".", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("."))
n0 = tkinter.Button(janela, text="0", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: digitar("0"))
eq = tkinter.Button(janela, text="=", font=("Arial", 18, "bold"), width=4, height=2, command=calcular_resultado)
o4 = tkinter.Button(janela, text="/", font=("Arial", 18, "bold"), width=4, height=2, command=lambda: operador("/", o4))

# Posicionamento
cl.grid(row=0, column=3)
n1.grid(row=1, column=0)
n2.grid(row=1, column=1)
n3.grid(row=1, column=2)
o1.grid(row=1, column=3)
n4.grid(row=2, column=0)
n5.grid(row=2, column=1)
n6.grid(row=2, column=2)
o2.grid(row=2, column=3)
n7.grid(row=3, column=0)
n8.grid(row=3, column=1)
n9.grid(row=3, column=2)
o3.grid(row=3, column=3)
ponto.grid(row=4, column=0)
n0.grid(row=4, column=1)
eq.grid(row=4, column=2)
o4.grid(row=4, column=3)

# Destaca o botão de operação pressionado
def destacar_operador(botao):
    resetar_cores_operadores()  # Reseta as cores primeiro
    botao.config(bg="green")

# Reseta os botões de operação para a cor padrão
def resetar_cores_operadores():
    for botao in botoes_operadores:
        botao.config(bg="lightgray")  # Cor padrão do sistema

# Adiciona os botões de operação à lista
botoes_operadores = [o1, o2, o3, o4]


# Inicia o loop
janela.mainloop()
