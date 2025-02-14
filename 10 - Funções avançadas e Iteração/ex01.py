def decorador(funcao):
    def interna():
        print("Código executado antes!")

        # Executa a função passada como parâmetro.
        funcao()

        print("Código executado depois!")
    return interna

@decorador
def minha_funcao():
    print("Minha função")


minha_funcao()