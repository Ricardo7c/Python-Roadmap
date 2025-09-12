from datetime import datetime, timedelta

data_hoje = datetime.now()
data_futura = data_hoje + timedelta(days=30)

print("Hoje:", data_hoje.strftime("%d/%m/%Y"))
print("Data daqui a 30 dias:", data_futura.strftime("%d/%m/%Y"))