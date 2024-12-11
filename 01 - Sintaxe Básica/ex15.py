# Solicita ao usuário um número inicial para a contagem regressiva
numero = int(input("Digite um número para começar a contagem regressiva: "))

while numero > 0:
    print(numero)  # Exibe o número atual
    # Pergunta ao usuário se deseja parar ou continuar
    comando = input('Digite "parar" para interromper ou pressione Enter para continuar: ')
    if comando.lower() == "parar":  # Verifica se o usuário quer parar
        print("Contagem interrompida!")
        break  # Sai do laço
    numero -= 1  # Decrementa o número

# Exibe uma mensagem se a contagem chegar ao fim
if numero == 0:
    print("Contagem finalizada!")
