def calcular_fibonacci(n):
    # Caso base: os dois primeiros números da sequência são 0 e 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: soma dos dois números anteriores
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

# Testes para diferentes valores de N
print(f"Fibonacci(5): {calcular_fibonacci(5)}")  # Saída esperada: 0# Saída esperada: 5
print(f"Fibonacci(10): {calcular_fibonacci(10)}")  # Saída esperada: 55
