import tkinter

def soma():
    n1 = int(num1.get())
    n2 = int(num2.get())
    texto.config(text=f"A soma é: {n1+n2}")
    


janela = tkinter.Tk()

janela.title("Somar numeros")
janela.geometry("300x200")


texto = tkinter.Label(janela, text="", font=("inpact",18))
texto.pack()

num1 = tkinter.Entry(janela, font=("Inpact", 18))
num1.pack(pady=10)
num2 = tkinter.Entry(janela, font=("Inpact", 18))
num2.pack(pady=10)
botao = tkinter.Button(text="Somar", command=soma).pack(expand=True)



janela.mainloop()