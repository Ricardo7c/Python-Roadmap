import re

def validar_email(email):
    # Define o padrão de regex para um e-mail válido
    padrao = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
    
    # Usa re.match para verificar se o e-mail segue o padrão
    if re.match(padrao, email):
        return True
    return False

# Testes da função
print(validar_email("usuario@dominio.com"))   # True
print(validar_email("usuario123@dominio.br")) # True
print(validar_email("usuario@@dominio.com"))  # False
print(validar_email("usuario@dominio"))       # False
print(validar_email("@dominio.com"))          # False
