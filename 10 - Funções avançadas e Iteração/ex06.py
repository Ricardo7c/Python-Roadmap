def meu_generador():
    for numero in range(10):
        yield numero * 2

# Usando o gerador
for value in meu_generador():
    print(value)