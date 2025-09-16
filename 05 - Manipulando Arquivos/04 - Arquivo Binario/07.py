import pickle

# Dados a serem serializados
lista = [1, 2, 3, 4, 5]
dicionario = {'nome': 'Ricardo', 'idade': 32}

# Nome do arquivo
nome_arquivo = 'dados.pkl'

# Serialização dos dados
with open(nome_arquivo, 'wb') as arquivo:
    pickle.dump(lista, arquivo)
    pickle.dump(dicionario, arquivo)

print(f"Dois objetos salvos em '{nome_arquivo}'")
