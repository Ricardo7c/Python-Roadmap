nomes = ["Ricardo", "Claudia", "João", "Marcia", "Debora"]
caminho = "04 - Bibliotecas e Arquivos/nomes.txt"

# Abrimos o arquivo(caminho) para escrita(w) com a codificação(utf-8)
with open(caminho, "w", encoding="utf-8") as arquivo:
    # Iteramos sobre a lista, escrevendo nome por nome
    for nome in nomes:
        arquivo.write(f"{nome}\n")
