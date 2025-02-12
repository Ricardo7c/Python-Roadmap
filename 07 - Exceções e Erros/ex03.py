# Exceção personalizada
class IdadeInvalidaError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

# Função para validar a idade
def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError("Idade menor que 18 não é permitida.")
    if idade > 100:
        raise IdadeInvalidaError("Idade maior que 100 não é permitida.")
    print("Idade válida!")

# Exemplo de uso
try:
    idade = int(input("Digite sua idade: "))
    validar_idade(idade)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
except ValueError:
    print("Erro: Por favor, insira um número válido.")
