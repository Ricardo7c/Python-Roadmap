# Definindo credenciais fixas
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

# Solicitando dados ao usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verificando credenciais
if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")