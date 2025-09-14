pessoa = {"nome": "Lucas", "idade": 28, "cidade": "São Paulo"}
chave = input("Digite a chave que deseja remover: ")

if chave in pessoa:
    valor_removido = pessoa.pop(chave)
    print("Valor removido:", valor_removido)
else:
    print("Chave não encontrada.")

print("Dicionário atualizado:", pessoa)
