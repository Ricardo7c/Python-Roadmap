# Crie um decorador chamado `repetir` que permita especificar quantas vezes uma função deve ser executada.

# Decorador que recebe um argumento
def repetir(vezes):

    # Decorador que recebe a função
    def decorator(func):

        # wrapper que recebe os argumentos da função
        def wrapper(*args, **kwargs):

            for _ in range(vezes):
                resultado = func(*args, **kwargs)     
            return resultado
        return wrapper
    return decorator        


@repetir(5) 
def saudacao():
    print(f'Olá!')      

saudacao()