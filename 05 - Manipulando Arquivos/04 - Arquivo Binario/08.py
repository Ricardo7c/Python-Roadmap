import pickle

# Certifique-se de que o arquivo 'dados.pkl' existe e foi criado
# no exercício anterior com dois objetos salvos.

# Abre o arquivo no modo de leitura binária ('rb')
with open('dados.pkl', 'rb') as arquivo:
    # Carrega o primeiro objeto (a lista)
    lista_carregada = pickle.load(arquivo)

    # Carrega o segundo objeto (o dicionário)
    dicionario_carregado = pickle.load(arquivo)

# Exibe os objetos carregados
print(f'Lista: {lista_carregada}')
print(f'Dicionário: {dicionario_carregado}')