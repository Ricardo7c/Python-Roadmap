class Funcionario:
    def __init__(self, nome: str, cargo: str, salario:float) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario = self.salario+(self.salario*(aumento/100))

class Gerente(Funcionario):
    def __init__(self, nome: str, cargo: str, salario: float, bonus:float) -> None:
        super().__init__(nome, cargo, salario)
        self.bonus = bonus
        self.salario += self.bonus

# ESSE MODULO É INUTIL!
    def aumentar_salario(self, aumento):
        return super().aumentar_salario(aumento)
    
funcionario = Funcionario("josé", "Auxiliar", 1400)
gerente = Gerente("Paulo", "Gerente", 1400, 200)

funcionario.aumentar_salario(20)
gerente.aumentar_salario(20)

print(f'{funcionario.salario:.2f}')
print(f'{gerente.salario:.2f}')