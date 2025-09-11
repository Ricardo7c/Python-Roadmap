def somar_elementos(lista):
    if not lista:
        return 0
    return lista[0] + somar_elementos(lista[1:])

# Teste
lista = [1,2,3,4]
print(f"Soma da lista {lista} é {somar_elementos(lista)}")