import csv

with open('produtos.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    cabecalho = next(leitor_csv)  # Ignora o cabeçalho
        
    dados = []
    for linha in leitor_csv:
        produto = linha[0]
        preco = float(linha[1])
        quantidade = int(linha[2])
        valor_total = preco * quantidade
        dados.append([produto, valor_total])

with open('relatorio.csv', 'w', newline='') as arquivo_relatorio:
    escritor_csv = csv.writer(arquivo_relatorio)
    escritor_csv.writerow(['produto', 'valor_total'])  # Escreve o cabeçalho
    escritor_csv.writerows(dados)  # Escreve os dados

# Uso da função
print("Relatório salvo em 'relatorio.csv'.")