import csv

with open('alunos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pula o cabeçalho
    for linha in leitor_csv:
        nome, idade, curso = linha
        print(f"Aluno: {nome} | Idade: {idade} | Curso: {curso}")