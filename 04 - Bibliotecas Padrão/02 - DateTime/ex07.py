from datetime import datetime, timedelta

futuro = input("Digite uma data futura (dd/mm/aaaa): ")

futuro_date = datetime.strptime(futuro, "%d/%m/%Y")
hoje = datetime.now()

diferenca = futuro_date - hoje

print(f"Faltam {diferenca.days} dias para essa data!")