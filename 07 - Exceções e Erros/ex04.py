import re

# Exceção personalizada para idade inválida
class IdadeInvalidaError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

# Exceção personalizada para nome inválido
class NomeInvalidoError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

# Função para validar a idade
def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError("Idade menor que 18 não é permitida.")
    if idade > 100:
        raise IdadeInvalidaError("Idade maior que 100 não é permitida.")
    print("Idade válida!")

# Função para validar o nome
def validar_nome(nome):
    # Verifica se o nome contém apenas letras e espaços
    if not re.match(r"^[A-Za-z\s]+$", nome):
        raise NomeInvalidoError("Nome contém caracteres inválidos. Use apenas letras e espaços.")
    print("Nome válido!")

# Função principal para cadastro
def cadastrar_usuario():
    try:
        # Solicita o nome do usuário
        nome = input("Digite seu nome: ")
        validar_nome(nome)

        # Solicita a idade do usuário
        idade = int(input("Digite sua idade: "))
        validar_idade(idade)

        print("Usuário cadastrado com sucesso!")

    except NomeInvalidoError as e:
        print(f"Erro: {e}")
    except IdadeInvalidaError as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Erro: Por favor, insira um número válido para a idade.")
    finally:
        print("Processo de cadastro concluído.")

# Executa o programa
if __name__ == "__main__":
    cadastrar_usuario()
