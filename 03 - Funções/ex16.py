def curta(nome):
    return f'Oi, {nome}!'

def longa(nome):
    return f'Oi {nome}, vamos aprender python juntos!'

# A função mensagem recebe outra função e a executa com o nome 'João'
def mensagem(funcao):
    return funcao('João')


print(mensagem(curta))

print(mensagem(longa))