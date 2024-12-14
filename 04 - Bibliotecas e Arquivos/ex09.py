import csv

caminho = "04 - Bibliotecas e Arquivos/arquivo.csv"

# Abrindo o arquivo em modo de escrita
with open(caminho, 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade', 'Cidade'])  # Escrevendo cabeçalhos
    escritor.writerow(['Ana', 25, 'Curitiba'])  # Escrevendo uma linha
    escritor.writerow(['Bruno', 30, 'São Paulo'])