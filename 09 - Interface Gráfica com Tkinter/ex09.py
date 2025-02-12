import tkinter as tk

def mostrar_hobbie():
    resultado = []
    if varLer.get():
        resultado.append("Ler")
    if varEsportes.get():
        resultado.append("Esportes")
    if varMusica.get():
        resultado.append("Musica")

    # Exibindo o estado no Label
    hobbies.config(text=", ".join(resultado))

# Criando a janela principal
janela = tk.Tk()
janela.title("Formulario de Hobbies")
janela.geometry("300x250")

# Variáveis para os checkboxes
varLer = tk.BooleanVar()
varEsportes = tk.BooleanVar()
varMusica = tk.BooleanVar()

# Criando os checkbuttons
ler = tk.Checkbutton(janela, text="Ler", variable=varLer)
esportes = tk.Checkbutton(janela, text="Esportes", variable=varEsportes)
musica = tk.Checkbutton(janela, text="Musica", variable=varMusica)

# Criando o botão
botao = tk.Button(janela, text="Mostrar Hobbie", command=mostrar_hobbie)

# Criando o label para mostrar os hobbies selecionados
hobbies = tk.Label(janela, font=("Impact", 18))

# Usando grid para um layout organizado
ler.grid(row=0, column=0, sticky="w", padx=10, pady=5)
esportes.grid(row=1, column=0, sticky="w", padx=10, pady=5)
musica.grid(row=2, column=0, sticky="w", padx=10, pady=5)

botao.grid(row=1, column=3, padx=52)

hobbies.grid(row=4, pady=10)
janela.grid_columnconfigure(3, weight=1)

janela.mainloop()
