def dividir_numeros():
    try:
        # Solicitar o primeiro número
        num1 = int(input("Digite o primeiro número: "))
        # Solicitar o segundo número
        num2 = int(input("Digite o segundo número: "))
        
        # Realizar a divisão
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    
    except ValueError:
        # Capturar erro de valor inválido
        print("Erro: Você deve inserir um número inteiro válido.")
    
    except ZeroDivisionError:
        # Capturar erro de divisão por zero
        print("Erro: Não é possível dividir por zero.")
    
    except Exception as e:
        # Capturar qualquer outro erro inesperado
        print(f"Erro inesperado: {e}")
    
# Executar a função
dividir_numeros()
