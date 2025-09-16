import pickle

msg = input("Digite uma mensagem: ")

with open('mensagem.bin', 'wb') as arquivo:
    pickle.dump(msg, arquivo)
    print("Frase salva em 'mensagem.bin'")



    