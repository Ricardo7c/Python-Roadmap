nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    status = "Aprovado"
elif 5 <= nota <= 6.9:
    status = "Recuperação"
else:
    status = "Reprovado"

print("Status:", status)