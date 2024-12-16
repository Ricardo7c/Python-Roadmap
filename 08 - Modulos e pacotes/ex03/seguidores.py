import requests

usuario = input("Digite o nome de usuario: ")


url = f"https://api.github.com/users/{usuario}/followers"
resposta = requests.get(url)
arquivo = resposta.json()

print("=== Lista de Seguidores ===")
for item in arquivo:
    print(item['login'])

