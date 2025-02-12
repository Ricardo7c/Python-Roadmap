import tkinter

janela = tkinter.Tk() # Cria a janela

janela.title("Menssagem de boas vindas!") # Adiciona um titulo na janela.
janela.geometry("400x300") # Especifica o tamanho e a posição da janela

 #Cria o texto dentro da janela
texto = tkinter.Label(janela, text="Bem vindo ao Tkinter!", font=("inpact",18))
texto.pack(expand=True) #Centraliza o texto no espaço disponivel




janela.mainloop() # Roda o programa
