class Produto:
    def __init__(self, nome:str, preco:float) -> None:
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, valor):
        self.preco -= (self.preco*(valor/100))

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Preço: {self.preco}"
    

peixe = Produto('Salmão', 25.50)
peixe.aplicar_desconto(30)
print(peixe)