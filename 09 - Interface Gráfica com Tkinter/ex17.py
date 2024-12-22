import tkinter

global tamanho

def aumentar():
    global tamanho
    tamanho += 1
    texto.config(font=("Arial", tamanho, "bold"))
    texto.update()

def diminuir():
    global tamanho
    tamanho -= 1
    texto.config(font=("Arial", tamanho, "bold"))
    texto.update()

def reset():
    global tamanho
    tamanho = 18
    texto.config(font=("Arial", tamanho, "bold"))
    texto.update()

janela = tkinter.Tk()
janela.geometry("300x300")
janela.title("Troca fonte do texto")

tamanho = 18
texto = tkinter.Label(janela, text="Texto de teste", font=("Arial", tamanho, "bold"))
texto.pack(pady=10)

b1 = tkinter.Button(text="Aumentar fonte", command=aumentar)
b1.pack(pady=10)
b2 = tkinter.Button(text="Diminuir fonte", command=diminuir)
b2.pack(pady=10)
b3 = tkinter.Button(text="Reset", command=reset)
b3.pack(pady=10)

janela.mainloop()