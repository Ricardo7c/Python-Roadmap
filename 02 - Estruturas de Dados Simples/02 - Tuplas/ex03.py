frutas = []

for i in range(5):
    fruta = input("Digite uma fruta: ")
    frutas.append(fruta)

tupla_frutas = tuple(frutas)
print("Tupla final:", tupla_frutas)
