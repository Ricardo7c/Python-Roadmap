import tkinter

def clique():
    texto.config(text="Botão clicado!")


janela = tkinter.Tk() # Cria a janela

janela.title("Um simples botão") # Adiciona um titulo na janela.
janela.geometry("400x300") # Especifica o tamanho e a posição da janela

 #Cria o texto dentro da janela
texto = tkinter.Label(janela, text="", font=("inpact",18))
texto.pack(expand=True) #Centraliza o texto no espaço disponivel

botao = tkinter.Button(janela, text="Click aqui", command=clique)
botao.pack(expand=True)




janela.mainloop() # Roda o programa