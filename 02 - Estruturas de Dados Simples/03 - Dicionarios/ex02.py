aluno = {"nome": "Ana", "idade": 22, "curso": "Java"}
chave = input("Digite a chave que deseja acessar: ")

if chave in aluno:
    print("O valor é:", aluno[chave])
else:
    print("Chave não encontrada.")
