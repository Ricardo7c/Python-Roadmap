def converter_distancia(km: float) -> float:
    """
    Converte uma distância de quilômetros para milhas.
    
    A conversão é feita utilizando a seguinte fórmula:
        milhas = quilômetros * 0.621371

    :param km: Distância em quilômetros (um número real não negativo).
    :return: A distância equivalente em milhas (um número real).
    
    Exemplo:
    >>> converter_distancia(10)
    6.21371
    """
    return km * 0.621371

# Testando a função
distancia_km = 10
distancia_milhas = converter_distancia(distancia_km)
print(f"{distancia_km} quilômetros equivalem a {distancia_milhas} milhas.")
