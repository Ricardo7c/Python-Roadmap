class Contato:
    def __init__(self, nome:str, telefone:str, email:str) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self) -> str:
        return f'Nome: {self.nome} Tel.:{self.telefone} E-mail: {self.email}'
    
    def __eq__(self, value: object) -> bool:
        return self.nome == value.nome and self.telefone == value.telefone and self.email == value.email

class Agenda:
    def __init__(self) -> None:
        self.lista = []

    def adicionar(self, contato: Contato):
        if contato in self.lista:
            print(f'{contato.nome} já está na lista')
        else:
            self.lista.append(contato)
        
    def remover(self, contato: Contato):
        if contato in self.lista:
            self.lista.remove(contato)
            print(f'{contato.nome} foi removido')
        else:
            print(f'{contato.nome} não esta na lista')

    def buscar(self, nome):
        for cada in self.lista:
            if cada.nome == nome:
                print(cada)

    def listar_contatos(self):
        ordenada = sorted(self.lista, key=lambda contato : contato.nome)
        for contato in ordenada:
            print(contato)


            

c1 = Contato('Google', '895632147', 'google@hotmail.com')
c2 = Contato('Microsoft', '984616498', 'microsoft@gmail.com')
c3 = Contato('Amanda', '656198432', 'amand2043@yahoo.com')
c4 = Contato('Zelia', '98491625', 'zeze354@ig.com')
c5 = Contato('Anita', '562323331', 'anita@gmail.com')

agenda = Agenda()

agenda.adicionar(c1)
agenda.adicionar(c2)
agenda.adicionar(c3)
agenda.adicionar(c4)
agenda.adicionar(c5)
agenda.adicionar(c4)


agenda.listar_contatos()
agenda.remover(c3)
print()
agenda.buscar('Ricardo')
print()
agenda.listar_contatos()
agenda.remover(c3)