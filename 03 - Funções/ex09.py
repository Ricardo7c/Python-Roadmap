def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# Teste
print(f"O 6º número de Fibonacci é {calcular_fibonacci(6)}")
print(f"O 10º número de Fibonacci é {calcular_fibonacci(10)}")