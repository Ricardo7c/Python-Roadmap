lista = [100, 200, 300, 400, 500]

for n in range (0,3):
    num = int(input(f"Digite o {n+1}º número: "))
    lista.insert(1, num)

print(lista)