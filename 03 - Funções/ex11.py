def somar_elementos(lista):
    # Caso base: se a lista estiver vazia, a soma é 0
    if not lista:
        return 0
    # Caso recursivo: soma o primeiro elemento com o restante da lista
    return lista[0] + somar_elementos(lista[1:])

lista = [1, 2, 3, 4, 5]
lista2 = [4, 2, 3]

print(f"{somar_elementos(lista)}")
print(f"{somar_elementos(lista2)}")