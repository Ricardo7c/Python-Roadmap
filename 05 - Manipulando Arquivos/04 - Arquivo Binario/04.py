import pickle

# Nome do arquivo binário
nome_arquivo = 'lista.pkl'

# Abre o arquivo em modo de leitura binária ('rb')
with open(nome_arquivo, 'rb') as arquivo:
    # Desserializa a lista do arquivo
    lista_carregada = pickle.load(arquivo)

# Exibe a lista carregada
print("Lista carregada:", lista_carregada)