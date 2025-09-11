def verificar_primo(n: int) -> bool:
    """Retorna True se n for primo, False caso contrário"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Teste
print(f"7 é primo: {verificar_primo(7)}")
print(f"10 é primo: {verificar_primo(10)}")
