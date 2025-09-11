def curta(nome):
    return f"Olá, {nome}! (mensagem curta)"

def longa(nome):
    return f"Olá, {nome}! Hoje foi um dia incrível e cheio de aprendizados! (mensagem longa)"

def mensagem(funcao, nome):
    print(funcao(nome))

# Teste
mensagem(curta, "João")
mensagem(longa, "João")
