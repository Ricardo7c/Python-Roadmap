class Carro:
    def __init__(self, marca:str, modelo:str, ano:int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0



    def acelerar(self):
        self.velocidade += 10
        return self.velocidade
    
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        return self.velocidade

carro = Carro('Citroen','Xsara Picasso', 2006)


carro.acelerar()
print(carro.velocidade)
carro.acelerar()
print(carro.velocidade)
carro.frear()
print(carro.velocidade)