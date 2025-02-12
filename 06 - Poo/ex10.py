class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        self.nome =nome
        self.idade = idade

    @property
    def categoria(self):
        if self.idade < 18:
            return "Menor de idade"
        else:
            return "Adulto"

ricardo = Pessoa("Ricardo", 34)

print(ricardo.categoria)