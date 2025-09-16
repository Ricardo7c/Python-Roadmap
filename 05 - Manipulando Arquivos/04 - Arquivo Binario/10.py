import pickle

# 1. Crie a estrutura de dados complexa
dados_complexos = {
    'id_projeto': 101,
    'status': 'Em Andamento',
    'tarefas': [
        {'id': 1, 'nome': 'Configurar ambiente', 'concluida': True},
        {'id': 2, 'nome': 'Desenvolver módulo', 'concluida': False},
        {'id': 3, 'nome': 'Testar funcionalidade', 'concluida': False}
    ],
    'equipe': {
        'lider': 'Maria Silva',
        'membros': ['João', 'Pedro', 'Ana']
    }
}

# 2. Salve o dicionário no arquivo 'complexo.pkl'
with open('complexo.pkl', 'wb') as arquivo:
    pickle.dump(dados_complexos, arquivo)
print("Objeto complexo salvo com sucesso.")

# 3. Carregue o dicionário do arquivo
with open('complexo.pkl', 'rb') as arquivo:
    dados_carregados = pickle.load(arquivo)

# 4. Verifique se os dados foram preservados
if dados_complexos == dados_carregados:
    print("Objeto complexo carregado com sucesso.")
    print("Dados originais e carregados são idênticos.")
else:
    print("Erro: Os dados carregados não correspondem aos originais.")