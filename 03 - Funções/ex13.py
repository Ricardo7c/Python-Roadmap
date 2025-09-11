def converter_distancia(km: float) -> float:
    """Converte uma distância em quilômetros para milhas"""
    return km * 0.621371

# Teste
print(f"10 km equivalem a {converter_distancia(10):.2f} milhas")