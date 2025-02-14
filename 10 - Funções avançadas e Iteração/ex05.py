class MeuIterador:
    def __init__(self, numeros):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        
        except IndexError:
            raise StopIteration



lista = [1, 2, 3]

for numero in MeuIterador(lista):
    print(numero)