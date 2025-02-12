import re

def extrair_numeros(texto):
    # Define o padrão de regex para capturar números inteiros e decimais
    padrao = r"\d+\.?\d*"
    
    # Usa re.findall para encontrar todos os números na string
    numeros = re.findall(padrao, texto)
    
    # Retorna a lista de números
    return numeros

# Testes da função
print(extrair_numeros("A conta é 123.45 e o código é 6789"))  # ['123.45', '6789']
print(extrair_numeros("Não há números aqui!"))               # []
print(extrair_numeros("2 maçãs custam 5.50 reais"))          # ['2', '5.50']
print(extrair_numeros("10, 20, e 30.5 são exemplos"))        # ['10', '20', '30.5']
