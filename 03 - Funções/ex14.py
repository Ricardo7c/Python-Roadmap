def verificar_primo(n: int) -> bool:
    """
    Verifica se um número inteiro positivo é primo.
    
    Um número é considerado primo se for maior que 1 e não for divisível
    por nenhum outro número além de 1 e ele mesmo.
    
    :param n: Número inteiro positivo a ser verificado.
    :return: Retorna True se o número for primo, caso contrário False.
    
    Exemplo:
    >>> verificar_primo(7)
    True
    >>> verificar_primo(10)
    False
    """
    # Caso base: números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    
    # Verificar divisibilidade de 2 até a raiz quadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Encontrou um divisor, portanto não é primo
    return True  # Se não encontrou divisores, o número é primo

# Testando a função
print(verificar_primo(7))   # Saída esperada: True
print(verificar_primo(10))  # Saída esperada: False
print(verificar_primo(1))   # Saída esperada: False
print(verificar_primo(11))  # Saída esperada: True
