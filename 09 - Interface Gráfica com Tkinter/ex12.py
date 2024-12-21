import tkinter

def selecionar():
    selecionado = listbox.curselection()
    if selecionado:
        item = listbox.get(selecionado[0])
        texto.config(text=f"{item}")
    else:
        texto.config(text="Nenhum item selecionado!")


janela = tkinter.Tk()
janela.geometry("300x200")
janela.title("Listbox no tkinter")

listbox = tkinter.Listbox(janela, height=5, width=20)
listbox.pack(padx=5, pady=15)

botao = tkinter.Button(text="Selecionar", command=selecionar)
botao.pack()

texto = tkinter.Label(font=("Arial", 15, "bold"))
texto.pack(pady=10)

lista = ["Maçã", "Banana", "Laranja", "Uva", "Pera"]

for fruta in lista:
    listbox.insert(tkinter.END, fruta)



janela.mainloop()