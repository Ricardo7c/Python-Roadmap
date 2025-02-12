class Livro:
    def __init__(self, titulo: str, autor:str, ano_publicacao:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self) -> str:
        return f'{self.titulo} - {self.autor} - {self.ano_publicacao}'

class Biblioteca:
    def __init__(self) -> None:
        self.lista = []

    def adicionar_livro(self, livro: Livro):
        self.lista.append(livro)


    def remover_livro(self, livro: Livro):
        if livro in self.lista:
            self.lista.remove(livro)
            print(f'{livro} (Removido)')
        else:
            print('Erro ao remover: Livro não encontrado')

    def buscar_livro(self, arg):
        for cada in self.lista:
            if cada.titulo.upper() == arg.upper() or cada.autor.upper() == arg.upper():
                return cada
        return None


livro1 = Livro('Literatura', 'Machado', 1980)
livro2 = Livro('Ficção', 'Asimov', 1970)
livro3 = Livro('Games', 'Zangado', 2017)
livro4 = Livro('Dogs', 'Luiza', 2015)

livraria = Biblioteca()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)
livraria.adicionar_livro(livro3)
livraria.adicionar_livro(livro4)


# livraria.remover_livro(livro3)

resultado = livraria.buscar_livro("Games")
if resultado == None:
    print(f'Livro não encontrado')
else:
    print(resultado)

print(livraria.buscar_livro('Ficção'))

livraria.remover_livro(livro3)
