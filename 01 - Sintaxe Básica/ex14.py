senha = "12345"
while True:
    entrada = input("Digite a senha para entrar: ")
    if entrada != senha:
        print("Senha incorreta, tente novamente!")
    else:
        print("Bem-vindo!")
        break;