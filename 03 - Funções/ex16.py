def dizer_oi(nome):
    return f'Oi, {nome}!'

def incentivar_aprender(nome):
    return f'Oi {nome}, vamos aprender python juntos!'


def mensagem_para_guilherme(funcao):
    return funcao('Guilherme')


print(mensagem_para_guilherme(dizer_oi))

print(mensagem_para_guilherme(incentivar_aprender))