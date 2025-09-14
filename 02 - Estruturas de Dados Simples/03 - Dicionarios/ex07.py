capital = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "França": "Paris",
    "Japão": "Tóquio"
}

pais = input("Digite o país: ")
capital_pais = capital.get(pais)

if capital_pais:
    print("A capital é:", capital_pais)
else:
    print("País não encontrado")