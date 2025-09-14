cores = ("vermelho", "azul", "verde", "amarelo", "preto")
indice = int(input("Digite um índice (0-4): "))

if 0 <= indice < len(cores):
    print("A cor selecionada é:", cores[indice])
else:
    print("Índice inválido.")