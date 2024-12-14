caminho = "04 - Bibliotecas e Arquivos/nomes.txt"

# Abrimos o arquivo com with open, eliminando assim a nescessidade do uso de close()
with open(caminho, "r", encoding="utf-8") as arquivo:
    # Iteramos sobre o texto
    for linha in arquivo:
        # Usamos end para remover a quebra de linha do print pois o texto ja tem quebra de linha
        print(linha, end="")