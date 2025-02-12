import tkinter
import time

def contador():
    texto.config(text="")
    texto.update()
    for cada in range(0, 6):
        time.sleep(1)
        tempo.config(text=f"{cada}")
        tempo.update()
    texto.config(text="Contagem finalizada!")

janela = tkinter.Tk()
janela.title("Cronometro")
janela.geometry("300x200")

tempo = tkinter.Label(janela, text="0", font=("Arial", 18, "bold"))
tempo.pack(pady=10)

botao = tkinter.Button(janela, text="INICIAR", command=contador)
botao.pack()

texto = tkinter.Label(janela, text="", font=("Arial", 18, "bold"))
texto.pack(pady=10)

janela.mainloop()