import tkinter
from tkinter import ttk
import time

janela = tkinter.Tk()
janela.geometry("400x200")
janela.title("Barra de progresso no tkinter")


barra = ttk.Progressbar(janela, orient="horizontal", length=100, mode="determinate")
barra.pack(pady=20)


def progresso():
    barra["maximum"] = 100
    for porcentagem in range(101):
        time.sleep(0.01)
        barra["value"] = porcentagem
        barra.update()


botao = ttk.Button(janela, text="Iniciar", command=progresso)
botao.pack(pady=20)



janela.mainloop()