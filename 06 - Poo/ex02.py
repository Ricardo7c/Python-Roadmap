class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura


    def calcular_area(self):
        return self.largura*self.altura
    
ret = Retangulo(5, 10)

print(ret.calcular_area())