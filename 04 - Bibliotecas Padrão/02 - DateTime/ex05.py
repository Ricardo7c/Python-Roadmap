from datetime import datetime

data = input("Digite uma data no formato dd/mm/aaaa: ")

data_formatada = datetime.strptime(data, "%d/%m/%Y")

print(f"Data convertida: ", data_formatada)