class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f'{self.nome} - R$ {self.preco:.2f}'

class Pedido:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover(self, produto: Produto):
        if produto in self.produtos:
            print(f'Removendo: {produto.nome}')
            self.produtos.remove(produto)
        else:
            print('Produto não encontrado no pedido.')

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total
    
    def exibir_pedido(self):
        for produto in self.produtos:
            print(produto)

produto1 = Produto("Pizza", 35.50)
produto2 = Produto("Refrigerante", 8.00)
produto3 = Produto("Sobremesa", 12.50)

pedido = Pedido()
pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
pedido.adicionar_produto(produto3)

pedido.exibir_pedido()
print()
pedido.remover(produto1)
print()
pedido.exibir_pedido()
print(f'Total: R${pedido.calcular_total():.2f}')