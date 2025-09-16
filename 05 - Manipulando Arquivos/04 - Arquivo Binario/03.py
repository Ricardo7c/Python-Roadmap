import pickle

# Dados a serem salvos
data = [1, 2, 3, 4, 5]

# Nome do arquivo
filename = 'lista.pkl'

# Abre o arquivo em modo de escrita binária ('wb') e salva a lista usando pickle.dump()
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Lista salva em '{filename}'")