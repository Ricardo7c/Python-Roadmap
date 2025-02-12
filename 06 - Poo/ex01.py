class Cachorro:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def latir(self):
        print('Au, Au!')


rex = Cachorro('Rex', 3)

rex.latir()
