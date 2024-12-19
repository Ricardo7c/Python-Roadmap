import tkinter

# Criando a janela principal
janela= tkinter.Tk()
janela.title("Dois frames")
janela.geometry("300x360")

frame1 = tkinter.Frame(janela, width=280, height=150, bg="gray")
frame1.pack(pady=10, padx=10)

frame2 = tkinter.Frame(janela, width=280, height=150, bg="gray")
frame2.pack(pady=10, padx=10)

# Adicionando o texto, usando place() para ocupar todo o espaço
texto = tkinter.Label(frame1, text="Área Superior", font=("Arial", 14), bg="gray")
texto.place(relx=0.5, rely=0.5, anchor="center")

botao = tkinter.Button(frame2, text="Clique aqui")
botao.place(width=100, height=40, relx=0.5, rely=0.5, anchor="center")



janela.mainloop()
