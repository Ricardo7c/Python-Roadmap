import re

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Compila a expressão regular para e-mails
email_regex = re.compile(r'[A-Za-z0-9\._-]+@[A-Za-z0-9-]+\.[A-Za-z0-9\.-]+')

# Encontra todos os e-mails na frase
emails_encontrados = email_regex.findall(frase)

# Exibe os e-mails encontrados
if emails_encontrados:
    print(f"E-mails encontrados: {emails_encontrados}")
else:
    print("Nenhum e-mail encontrado na frase.")