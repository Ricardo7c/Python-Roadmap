import csv

with open('alunos.csv', 'a', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Marina', '20', 'Arquitetura'])

print("Novo aluno adicionado ao arquivo.")