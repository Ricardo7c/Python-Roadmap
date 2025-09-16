import pickle

# Dados do usuário
usuario = {
    'nome': 'Ricardo',
    'idade': 30,
    'email': 'ricardo@example.com'
}

# Nome do arquivo
nome_arquivo = 'usuario.pkl'

# Serializa e salva o dicionário no arquivo
with open(nome_arquivo, 'wb') as arquivo:
    pickle.dump(usuario, arquivo)

print(f"Dicionário salvo em '{nome_arquivo}'")