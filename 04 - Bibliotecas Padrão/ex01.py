import random

# Gerar o número aleatório entre 1 e 10
numero = random.randint(1, 10)

# Variável para contar as tentativas
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

# Loop para o jogo
while True:
    # Solicitar o palpite do jogador
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1  # Incrementar o número de tentativas

    # Verificar o palpite
    if palpite < numero:
        print("O número é maior. Tente novamente.")
    elif palpite > numero:
        print("O número é menor. Tente novamente.")
    else:
        # Caso o palpite esteja correto
        print(f"Parabéns! Você acertou.")
        print(f"Numero de tentativas: {tentativas}")
        break  # Finaliza o jogo quando o jogador acerta
