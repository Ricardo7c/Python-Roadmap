def decorador(funcao):
    # Função interna que recebe os argumentos da função decorada.
    def interna(*args, **kwargs):
        print("Bem vindo!")

        # A função decorada recebe de volta os argumentos passados para a função interna.
        funcao(*args, **kwargs)

        print("pode ficar a vontade!")
    return interna


@decorador
def nome(nome):
    print(nome, end=', ')



nome("João")