import tkinter

janela = tkinter.Tk()
janela.title("Jogo da velha")
janela.geometry("400x400")


b1 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=0, column=0)
b2 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=0, column=1)
b3 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=0, column=2)
b4 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=1, column=0)
b5 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=1, column=1)
b6 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=1, column=2)
b7 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=2, column=0)
b8 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=2, column=1)
b9 = tkinter.Button(font=("Arial", 25, "bold")).grid(row=2, column=2)



janela.mainloop()