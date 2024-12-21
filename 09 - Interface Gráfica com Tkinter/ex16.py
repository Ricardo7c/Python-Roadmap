import tkinter

# Função para iniciar o desenho
def iniciar_desenho(event):
    global ultima_posicao
    ultima_posicao = (event.x, event.y)  # Salva a posição inicial do mouse

# Função para desenhar enquanto o mouse é arrastado
def desenhar(event):
    global ultima_posicao
    x1, y1 = ultima_posicao  # Recupera a última posição
    x2, y2 = event.x, event.y  # Nova posição do mouse
    canvas.create_line(x1, y1, x2, y2, fill="black", width=3)  # Desenha uma linha
    ultima_posicao = (x2, y2)  # Atualiza a última posição

# Função para limpar o Canvas
def limpar_canvas():
    canvas.delete("all")  # Remove todos os objetos do Canvas

# Janela principal
janela = tkinter.Tk()
janela.title("Desenho com Canvas")
janela.geometry("800x600")

# Canvas onde o desenho será feito
canvas = tkinter.Canvas(janela, width=800, height=550, bg="white")
canvas.pack()

# Botão para limpar o Canvas
botao = tkinter.Button(janela, text="Limpar", command=limpar_canvas)
botao.pack(pady=10)

# Eventos do mouse
canvas.bind("<Button-1>", iniciar_desenho)  # Clique para iniciar o desenho
canvas.bind("<B1-Motion>", desenhar)  # Arraste para desenhar

# Executando a interface
janela.mainloop()
