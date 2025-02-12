class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def fazer_som(self):
        print('Som do animal')

class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def fazer_som(self):
        print('Miau')



vilma = Gato('Vilma')

vilma.fazer_som()