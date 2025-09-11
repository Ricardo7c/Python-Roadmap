def calcular_desconto(preco: float, desconto: float) -> float:
    """
    Calcula o preço final aplicando desconto percentual.
    preco: preço original
    desconto: porcentagem de desconto (0-100)
    """
    return preco * (1 - desconto/100)

# Teste
print(f"Preço original: 200, Desconto: 10% → Preço final: {calcular_desconto(200,10)}")
