from datetime import datetime, timedelta

nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")

nasc_formatada = datetime.strptime(nasc, "%d/%m/%Y")

hoje = datetime.now()

idade = hoje - nasc_formatada

print(f"Você já viveu {idade.days} dias!")