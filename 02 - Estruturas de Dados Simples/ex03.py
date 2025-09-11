turma1 = []
turma2 = []

for n in range(0, 3):
    nome = input(f"Digite um aluno da turma 1: ")
    turma1.append(nome)

for n in range(0, 2):
    nome = input(f"Digite um aluno da turma 2: ")
    turma2.append(nome)

turma1.extend(turma2)
print("Turma completa: ", turma1)