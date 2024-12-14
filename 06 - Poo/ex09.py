class Matematica:

    @classmethod
    def fatorial(cls, n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    @staticmethod
    def multiplicar(a, b):
        return a*b
    
mat = Matematica()

print(mat.fatorial(5))
print(mat.multiplicar(4,6))