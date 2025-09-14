produto = {"nome": "Camiseta", "preco": 50, "quantidade": 10}

produto["preco"] = float(input("Digite o novo preço: "))
produto["quantidade"] = int(input("Digite a nova quantidade: "))

print("Produto atualizado:", produto)