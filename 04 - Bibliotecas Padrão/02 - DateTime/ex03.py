from datetime import datetime

atual = datetime.now()

nome = input("Digite seu nome: ")

print(f"Bem vindo, {nome}! Hoje é {atual.strftime('%d/%m/%Y')}.")