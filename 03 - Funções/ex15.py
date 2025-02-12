def calcular_desconto(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final de um produto após aplicar um desconto.
    
    O desconto é calculado multiplicando o preço original pela porcentagem de desconto
    e subtraindo o valor do desconto do preço original.
    
    :param preco_original: Preço original do produto (um número real positivo).
    :param percentual_desconto: Percentual de desconto (um número real entre 0 e 100).
    :return: O preço final do produto após aplicar o desconto.
    
    Exemplo:
    >>> calcular_desconto(100, 20)
    80.0
    >>> calcular_desconto(150, 10)
    135.0
    """
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final

# Testando a função
print(calcular_desconto(100, 20))  # Saída esperada: 80.0
print(calcular_desconto(150, 10))  # Saída esperada: 135.0
