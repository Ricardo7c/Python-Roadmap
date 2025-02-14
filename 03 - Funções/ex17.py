
# A função pai define e chama duas funções filhas.
def pai():
    print('Escrevendo da função pai')
    
    # As funções filhas só existem dentro da função pai.
    # Não é possível chamá-las fora da função pai.
    def filha1():
        print('Escrevendo da função filha1')
    
    def filha2():
        print('Escrevendo da função filha2')

    # A ordem de execução das funções filhas é a ordem de chamada.
    filha2()
    filha1()


# Chamando a função pai e consequentemente as duas filhas.
pai()