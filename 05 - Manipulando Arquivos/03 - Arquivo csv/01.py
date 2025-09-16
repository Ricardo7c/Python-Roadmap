import csv

# Dados dos alunos
dados = [
    {'nome': 'Alice', 'idade': 20, 'curso': 'Engenharia'},
    {'nome': 'Bob', 'idade': 22, 'curso': 'Ciência da Computação'},
    {'nome': 'Carol', 'idade': 19, 'curso': 'Medicina'}
]

# Escreve os dados no arquivo CSV
with open('alunos.csv', 'w', newline='') as arquivo_csv:

    # Define o cabeçalho
    cabecalho = ['nome', 'idade', 'curso']
    
    # Cria o formato do conteudo
    conteudo = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)

    # Escreve o cabeçalho
    conteudo.writeheader()

    # Escreve os dadosS
    conteudo.writerows(dados)

print(f"Arquivo 'alunos.csv' criado com 3 registros.")