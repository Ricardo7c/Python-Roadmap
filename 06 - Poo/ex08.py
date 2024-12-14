class Livro:
    def __init__(self, titulo:str, autor:str, ano:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano


    def __eq__(self, value: object) -> bool:
        if isinstance(value, Livro):
            return self.titulo == value.titulo and self.autor == value.autor
        return False


l1 = Livro("Pense em python", "Luciano Ramalho", 2015)
l2 = Livro("Python Fluente", "Luciano Ramalho", 2015)
l3 = Livro("Pense em python", "Luciano Ramalho", 2015)


print(l1 == l3)