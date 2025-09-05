import tkinter as tk

# Função para verificar se há um vencedor
def verificar_vencedor():
    combinacoes = [
        [b1, b2, b3],  # Linha 1
        [b4, b5, b6],  # Linha 2
        [b7, b8, b9],  # Linha 3
        [b1, b4, b7],  # Coluna 1
        [b2, b5, b8],  # Coluna 2
        [b3, b6, b9],  # Coluna 3
        [b1, b5, b9],  # Diagonal 1
        [b3, b5, b7],  # Diagonal 2
    ]
    
    for combinacao in combinacoes:
        valores = [botao["text"] for botao in combinacao]
        if valores == ["X", "X", "X"]:
            finalizar_jogo("X venceu!")
            return
        elif valores == ["O", "O", "O"]:
            finalizar_jogo("O venceu!")
            return
    
    # Verifica se todos os botões estão preenchidos (empate)
    if all(botao["text"] in ["X", "O"] for botao in botoes):
        finalizar_jogo("Empate!")

# Função para finalizar o jogo
def finalizar_jogo(mensagem):
    for botao in botoes:
        botao.config(state="disabled")
    jogador.config(text=mensagem)

# Função para realizar a jogada
def jogada(botao):
    global vez
    global jogador
    if botao["text"] == "":
        if vez:
            botao.config(text="X", state="disabled")
            vez = False
            jogador_atual = "O"
        else:
            botao.config(text="O", state="disabled")
            vez = True
            jogador_atual = "X"
            
        jogador.config(text=f"vez do {jogador_atual}")
        verificar_vencedor()
    

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("300x270")
janela.title("Jogo da Velha")
janela.resizable(False, False)

vez = True  # Variável global para alternar entre os jogadores

# Criando os botões
b1 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b1))
b2 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b2))
b3 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b3))
b4 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b4))
b5 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b5))
b6 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b6))
b7 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b7))
b8 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b8))
b9 = tk.Button(janela, font=("Arial", 18, "bold"), width=4, height=2, command=lambda: jogada(b9))

# Lista para facilitar iterações
botoes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# Organizando os botões em uma grade
b1.grid(row=1, column=0, padx=2, pady=2)
b2.grid(row=1, column=1, padx=2, pady=2)
b3.grid(row=1, column=2, padx=2, pady=2)
b4.grid(row=2, column=0, padx=2, pady=2)
b5.grid(row=2, column=1, padx=2, pady=2)
b6.grid(row=2, column=2, padx=2, pady=2)
b7.grid(row=3, column=0, padx=2, pady=2)
b8.grid(row=3, column=1, padx=2, pady=2)
b9.grid(row=3, column=2, padx=2, pady=2)

jogador = tk.Label(janela, text="X começa", font=("Arial", 14))
jogador.grid(row=0, column=0)

# Inicia o loop da interface
janela.mainloop()
