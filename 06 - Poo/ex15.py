class ItemEstoque:
    def __init__(self, nome:str, quantidade:int, preco_por_unidade:float) -> None:
        self.nome = nome
        self.quantidade = quantidade
        self.preco_por_unidade = preco_por_unidade

class Estoque:
    def __init__(self) -> None:
        self.estoque = []

    def adicionar(self, item:ItemEstoque):
        self.estoque.append(item)

    def remover(self, item:ItemEstoque):
        if item in self.estoque:
            item.quantidade -= 1
            if item.quantidade <= 0:
                self.estoque.remove(item)

    def mostrar_items(self):
        for cada in self.estoque:
            print(f'Nome: {cada.nome} - {cada.quantidade}')

    def atualizar_quantidade(self, item:ItemEstoque, qt:int):
        if item in self.estoque:
            item.quantidade += qt

    def calcular_estoque_total(self):
        total = sum(item.preco_por_unidade*item.quantidade for item in self.estoque)
        return total

    def buscar_estoque_baixo(self, limite = 2):
        precisaRepor = [item for item in self.estoque if item.quantidade <= limite]
        return precisaRepor


item1 = ItemEstoque('Notebook', 3, 2.500)
item2 = ItemEstoque('Celular', 3, 4.300)

estoque = Estoque()

estoque.adicionar(item1)
estoque.adicionar(item2)

estoque.remover(item1)
estoque.remover(item1)
estoque.remover(item2)
estoque.atualizar_quantidade(item2, 3)
total = estoque.calcular_estoque_total()
print(f'O Valor total do estoque é: R${total:.3f}')

estoque.mostrar_items()
print()

repor = estoque.buscar_estoque_baixo(2)
if len(repor) > 0:
    print(f'Numero de itens com estoque baixo: {len(repor)}')
    for item in repor:
        print(f'{item.nome} - {item.quantidade}')