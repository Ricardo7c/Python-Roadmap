import requests

# URL da API do GitHub para o repositório
url = "https://api.github.com/repos/Ricardo7c/Python-Roadmap"

# Fazer a requisição GET
response = requests.get(url)


# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # converter a requisição para o formato de dicionario usando o metodo .json()
    data = response.json()

    # Exibi as informações desejadas
    print(f"Nome do repositório: {data['name']}")
    print(f"Descrição: {data['description']}")
else:
    # Caso ocorra algum erro na requisição
    print("Erro ao acessar a API do GitHub:", response.status_code)
