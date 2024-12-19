import tkinter

def trocar_cor(cor):
    janela.config(bg=cor)


janela = tkinter.Tk() # Cria a janela

janela.title("Mudar cores") # Adiciona um titulo na janela.
janela.geometry("400x300") # Especifica o tamanho e a posição da janela


botao1 = tkinter.Button(janela, text="Vermelho", background=("#FF5733"), command=lambda: trocar_cor("#FF5733"))
botao1.pack(expand=True)

botao3 = tkinter.Button(janela, text="Verde", background=("#32CD32"), command=lambda: trocar_cor("#32CD32"))
botao3.pack(expand=True)

botao2 = tkinter.Button(janela, text="Azul", background=("#1E90FF"), command=lambda: trocar_cor("#1E90FF"))
botao2.pack(expand=True)






janela.mainloop() # Roda o programa