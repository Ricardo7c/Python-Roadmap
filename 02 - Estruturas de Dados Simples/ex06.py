nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nome_para_contar = input("Digite um nome para contar: ")
ocorrencias = nomes.count(nome_para_contar)

print(f"O nome aparece {ocorrencias} vezes na lista.")