class Tarefa:
    def __init__(self, descricao: str, concluida:bool = False) -> None:
        self.descricao = descricao
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def alterar_descricao(self, descricao:str):
        if descricao:
            self.descricao = descricao

    def __str__(self) -> str:
        status = 'CONCLUIDA' if self.concluida else 'PENDENTE'
        return f'{self.descricao} - {status}'

class ListaDeTarefas:
    def __init__(self) -> None:
        self.lista = []

    def adicionar(self, tarefa: Tarefa):
        self.lista.append(tarefa)

    def remover(self, tarefa: Tarefa):
        if tarefa in self.lista:
            self.lista.remove(tarefa)
    
    def listar_todas(self):
        print('Lista de tarefas:')
        for tarefa in self.lista:
            print(tarefa)

    def listar_concluidas(self):
        concluidas = [tarefa for tarefa in self.lista if tarefa.concluida]
        print(f'{len(concluidas)} - tarefas concluidas:')
        for tarefa in concluidas:
            print(tarefa),

t1 = Tarefa('pagar boletos')
t2 = Tarefa('Fazer mercado')
t3 = Tarefa('pedir pizza')


lista = ListaDeTarefas()
lista.adicionar(t1)
lista.adicionar(t2)
lista.adicionar(t3)

lista.listar_todas()

t1.concluir()
t2.concluir()
t3.alterar_descricao('')
print()
lista.listar_todas()
print()
lista.listar_concluidas()
