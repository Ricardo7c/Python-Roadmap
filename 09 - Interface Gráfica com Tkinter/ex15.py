import tkinter
from tkinter import filedialog

janela = tkinter.Tk()
janela.geometry("300x200")
janela.title("Caixas de Dialogo")

def abrir():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[("Todos os arquivos", "*"),("Arquivos de texto", "*.txt")]
    )
    
    if arquivo:
        texto.config(text=arquivo)
    else:
        texto.config("Nenhum arquivo selecionado.")
    

botao = tkinter.Button(janela, text="Abrir Arquivo", command=abrir)
botao.pack(pady=20)


texto = tkinter.Label(janela, text="Nenhum arquivo selecionado.", wraplength=350, justify="left")
texto.pack(pady=10)




janela.mainloop()