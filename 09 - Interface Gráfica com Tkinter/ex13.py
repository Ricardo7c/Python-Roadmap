import tkinter

def escolha():
    texto.config(text=f"{selecao.get()}")


janela = tkinter.Tk()
janela.geometry("300x200")
janela.title("Radiobutton no tkinter")

selecao = tkinter.StringVar(value="Primeira opção")

rb1 = tkinter.Radiobutton(janela, text="Opção 1", variable=selecao, value="Primeira opção", command=escolha)
rb1.pack()
rb2 = tkinter.Radiobutton(janela, text="Opção 2", variable=selecao, value="Segunda opção", command=escolha)
rb2.pack()
rb3 = tkinter.Radiobutton(janela, text="Opção 3", variable=selecao, value="Terceira opção", command=escolha)
rb3.pack()

texto = tkinter.Label(janela, text="Primeira opção")
texto.pack()

janela.mainloop()