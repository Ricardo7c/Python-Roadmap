from datetime import datetime, timedelta

data_hoje = datetime.now()

aniv = input("Qual a data do seu proximo aniversario (dd/mm/aaaa): ")

aniv_date = datetime.strptime(aniv, "%d/%m/%Y")

dias_faltando = (aniv_date - data_hoje).days

print(f"Faltam {dias_faltando} dias para o seu proximo aniversario.")