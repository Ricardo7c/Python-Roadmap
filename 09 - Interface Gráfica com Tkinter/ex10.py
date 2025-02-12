import tkinter

def trocar_cor(cor):
    janela.config(bg=cor)
    texto.config(text=f"{cor}", bg=cor)


janela = tkinter.Tk()  # Cria a janela

janela.title("Mudar cores")  # Adiciona um título na janela.
janela.geometry("250x100")  # Especifica o tamanho e a posição da janela
janela.config(bg="Red")

# Criando os botões
botao1 = tkinter.Button(janela, text="Red", background="Red", command=lambda: trocar_cor("Red"))
botao1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

botao2 = tkinter.Button(janela, text="Green", background="Green", command=lambda: trocar_cor("Green"))
botao2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

botao3 = tkinter.Button(janela, text="Yellow", background="Yellow", command=lambda: trocar_cor("Yellow"))
botao3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Label para exibir o texto
texto = tkinter.Label(janela, text="Red", font=("Impact", 18), bg="Red")
texto.grid(row=1, column=0, columnspan=3, pady=5, sticky="nsew")

# Tornando as linhas e colunas responsivas
janela.grid_rowconfigure(0, weight=1)  # Linha 0 (botões) vai se expandir
janela.grid_rowconfigure(1, weight=1)  # Linha 1 (label) vai se expandir

janela.grid_columnconfigure(0, weight=1)  # Coluna 0 vai se expandir
janela.grid_columnconfigure(1, weight=1)  # Coluna 1 vai se expandir
janela.grid_columnconfigure(2, weight=1)  # Coluna 2 vai se expandir

janela.mainloop()  # Roda o programa
