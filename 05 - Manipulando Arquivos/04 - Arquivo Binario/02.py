import pickle

with open('mensagem.bin', 'rb') as arquivo:
    mensagem = pickle.load(arquivo)
    print(f"Conteúdo lido: {mensagem}")
