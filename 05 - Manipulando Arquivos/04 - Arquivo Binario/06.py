import pickle

with open('usuario.pkl', 'rb') as arquivo:
    usuario = pickle.load(arquivo)
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
