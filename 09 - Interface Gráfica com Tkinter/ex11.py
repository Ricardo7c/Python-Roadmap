import tkinter

def update_texto(valor):
    texto.config(text=f"{valor}")


janela = tkinter.Tk()
janela.geometry("300x200")
janela.title("Slider no tkinter")


slider = tkinter.Scale(janela, from_=0, to=100, orient="horizontal", command=update_texto)
slider.pack()

texto = tkinter.Label(janela, text="0", font=("Arial", 50, "bold"))
texto.pack()


janela.mainloop()