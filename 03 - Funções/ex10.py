def contar_regressivo(n):
    if n < 0:
        return
    print(n)
    contar_regressivo(n-1)

# Teste
contar_regressivo(5)