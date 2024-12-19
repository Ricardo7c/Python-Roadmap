import tkinter

def clique():
    valor = caixa_texto.get()
    texto.config(text=valor)


janela = tkinter.Tk() # Cria a janela

janela.title("Meu texto") # Adiciona um titulo na janela.
janela.geometry("400x300") # Especifica o tamanho e a posição da janela

 #Cria o texto dentro da janela
texto = tkinter.Label(janela, text="", font=("inpact",18))
texto.pack(expand=True) #Centraliza o texto no espaço disponivel

caixa_texto = tkinter.Entry(janela, font=("Arial", 14))
caixa_texto.pack(expand=True)

botao = tkinter.Button(janela, text="Click aqui", command=clique)
botao.pack(expand=True)




janela.mainloop() # Roda o programa