from datetime import datetime

# Solicitar as datas ao usuário
data_1 = input("Digite a primeira data (DD/MM/AAAA): ")
data_2 = input("Digite a segunda data (DD/MM/AAAA): ")

# Converter as strings para objetos datetime
data_1 = datetime.strptime(data_1, "%d/%m/%Y")
data_2 = datetime.strptime(data_2, "%d/%m/%Y")

# Calcular a diferença em dias
diferenca = abs((data_2 - data_1).days)

# Exibir o resultado
print(f"A diferença entre as duas datas é de {diferenca} dias.")
