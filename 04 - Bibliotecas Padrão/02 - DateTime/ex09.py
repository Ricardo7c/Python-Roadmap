from datetime import datetime, timedelta

data_hoje = datetime.now()
data_passada = data_hoje - timedelta(days=100)

print("A data de 100 dias atrás era:", data_passada.strftime("%d/%m/%Y"))