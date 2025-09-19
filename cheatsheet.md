# 🐍 **Python Cheat Sheet**

## 🚀 Estrutura Básica

```python
print("Hello, Python!")
```

---

## 🔹 Variáveis e Tipos

```python
x = 10          # int
y = 3.14        # float
nome = "Ana"    # str
ativo = True    # bool
nulo = None     # NoneType
```

---

## 🔹 Operadores

```python
# Aritméticos
+, -, *, /, // (divisão inteira), % (módulo), ** (potência)

# Relacionais
==, !=, >, <, >=, <=

# Lógicos
and, or, not
```

---

## 🔹 Estruturas de Controle

```python
if x > 0:
    print("Positivo")
elif x == 0:
    print("Zero")
else:
    print("Negativo")

# Condicional em uma linha
status = "Maior" if x > 18 else "Menor"
```

---

## 🔹 Laços

```python
for i in range(5):
    print(i)

while x > 0:
    x -= 1
```

---

## 🔹 Coleções

```python
lista = [1, 2, 3]
lista.append(4)

tupla = (1, 2, 3)

conjunto = {1, 2, 3}
conjunto.add(4)

dicionario = {"nome": "Ana", "idade": 25}
print(dicionario["nome"])
```

<details>
<summary>Extras úteis</summary>

```python
# List comprehension
quadrados = [x**2 for x in range(5)]

# Dict comprehension
mapa = {x: x**2 for x in range(5)}
```

</details>

---

## 🔹 Funções

```python
def soma(a, b=0):
    return a + b

def saudacao(nome, idade=18):
    print(f"Olá {nome}, idade {idade}")

# Lambda
dobro = lambda x: x * 2
```

---

## 🔹 Classes e Objetos

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome}")

p = Pessoa("Ana", 25)
p.falar()
```

---

## 🔹 Herança

```python
class Animal:
    def som(self):
        print("Som genérico")

class Cachorro(Animal):
    def som(self):
        print("Au au")

c = Cachorro()
c.som()
```

---

## 🔹 Exceções

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero!")
except Exception as e:
    print("Erro:", e)
finally:
    print("Fim")
```

---

## 🔹 Arquivos

```python
# Escrita
with open("teste.txt", "w") as f:
    f.write("Olá Python!")

# Leitura
with open("teste.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
```

---

## 🔹 JSON

```python
import json

# String para objeto
data = '{"nome": "Ana", "idade": 25}'
obj = json.loads(data)
print(obj["nome"])

# Objeto para string
novo = {"cidade": "SP", "pop": 12345}
print(json.dumps(novo))
```

---

## 🔹 Módulos Úteis

```python
import math, random, datetime, os, sys, re

print(math.sqrt(16))   # 4.0
print(random.randint(1, 10))
print(datetime.date.today())
```

---

## 🔹 Iteradores e Geradores

```python
# Iterador
for c in "Python":
    print(c)

# Gerador
def contador():
    for i in range(3):
        yield i

for n in contador():
    print(n)
```

---

## 🔹 Decoradores

```python
def log(func):
    def wrapper():
        print("Iniciando...")
        func()
        print("Finalizando...")
    return wrapper

@log
def teste():
    print("Função executada!")

teste()
```

---

## 🔹 Virtual Env & Pacotes

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar pacotes
pip install requests

# Exportar dependências
pip freeze > requirements.txt
```

---

📌 Esse cheat sheet cobre o essencial até intermediário/avançado.
