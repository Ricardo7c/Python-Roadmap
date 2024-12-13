preco = float(input("Digite o preço original do produto: "))
desc = int(input("Digite a porcetagem do desconto: "))

valor_desconto = preco*(desc/100)

print(f"O produto custa R${preco:.2f} mas com desconto de {desc}% fica por R${preco-valor_desconto:.2f}")