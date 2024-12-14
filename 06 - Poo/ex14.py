class Quarto:
    def __init__(self,numero: int, tipo:str, preco_por_noite: float, disponibilidade: bool = True) -> None:
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite
        self.disponibilidade = disponibilidade

class Reserva:
    def __init__(self, noites: int) -> None:
        self.noites = noites
        
    def custo_total(self, quarto:Quarto):
        if quarto.disponibilidade:
            total = quarto.preco_por_noite * self.noites
            quarto.disponibilidade = False
            return f'Custo total: R${total:.2f}'
        return 'Quarto indisponível'
    

q1 = Quarto(1, 'Solteiro', 300)
q2 = Quarto(2, 'Solteiro', 300)
r1 = Reserva(5)
r2 = Reserva(4)

print(r1.custo_total(q1))
print(r2.custo_total(q2))