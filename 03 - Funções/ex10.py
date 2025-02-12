def contar_regressivo(num):
    print(num)
    if num > 0:
        contar_regressivo(num-1)


num = 5
contar_regressivo(5)


