def decorador(funcao):
    def interna(*args, **kwargs):
        print("Iniciando a função...")
        resultado = funcao(*args, **kwargs)  # Armazena o retorno da função decorada
        print("Função finalizada!")
        return resultado  # Retorna o valor original da função decorada
    return interna


@decorador
def saudacao(nome):
    return f"Olá, {nome}!"


mensagem = saudacao("Ricardo")
print(mensagem)
