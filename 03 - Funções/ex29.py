lista = [0, 1, "", "Texto", [], [1]]
for elemento in lista:
    if elemento:
        print(f"{elemento} -> True")
    else:
        print(f"{elemento} -> False")