# Nome dos arquivos
arquivo_origem = 'mensagem.bin'
arquivo_destino = 'copia.bin'

# Abre o arquivo de origem para leitura binária ('rb')
with open(arquivo_origem, 'rb') as f_origem:
    # Lê todo o conteúdo do arquivo
    conteudo = f_origem.read()

# Abre o arquivo de destino para escrita binária ('wb')
with open(arquivo_destino, 'wb') as f_destino:
    # Escreve o conteúdo lido no novo arquivo
    f_destino.write(conteudo)

print(f"Arquivo '{arquivo_origem}' copiado para '{arquivo_destino}'")