class Pessoa:
    contador = 0

    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade
        Pessoa.contador += 1

    @classmethod
    def informar_total_pessoas(cls):
        return cls.contador
    

p1 = Pessoa('Ricardo', 34)
p2 = Pessoa('Claudia', 50)
p3 = Pessoa('João', 25)

print(Pessoa.informar_total_pessoas())