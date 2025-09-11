# **Python Roadmap: Sua Jornada no Mundo do Python**  

Este roadmap foi criado por mim para auxiliar nos meus estudos em Python.

**NÃO É UM CURSO:** Apenas um guia para organizar os estudos.

Sugiro seguir o roadmap sem pular etapas, garantindo que cada tópico seja compreendido antes de prosseguir. Python é uma linguagem versátil e intuitiva, mas construir uma base sólida é essencial.

🚀 **Pronto para começar sua jornada com Python?**


## 🌱 Conselhos Gerais

* **Prática Constante**: resolver exercicios ou problemas reais é melhor que decorar sintaxe.
* **Foque no Básico Primeiro**: não tente aprender tudo de uma vez.
* **Use a Documentação**: docs oficiais do Python e bibliotecas sempre serão seu melhor guia.
* **Siga o Zen de Python**: simplicidade e clareza > complexidade.
* **Construa Projetos**: mesmo pequenos, eles fixam o aprendizado.
* **Compartilhe Código**: publique no GitHub, peça feedback, colabore em comunidades além de se familiarizar com o git/github, você ainda gera portifólio.

## **INTRODUÇÃO**

   * **O que é Python e sua Filosofia** *(PEP 20 - Zen de Python)* - [Documentário](https://youtu.be/GfH4QL4VqJ0)
   * **Instalação do Python** - [Download](https://www.python.org/downloads/)
   * **Uso do VS Code** - [Download](https://code.visualstudio.com/)
   * **Shell interativo vs script** *(python3, arquivo.py)*

## 🟢 **NÍVEL BÁSICO**

### 1. Sintaxe Básica - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/01%20-%20Sintaxe%20B%C3%A1sica)

* **Saida de dados** (print, f-strings)
* **Variáveis, tipos e conversão de tipos** (int, float, str, bool)
* **Entrada de dados** (input)
* **Operadores Aritméticos** (+, -, *, /)
* **Operadores Relacionais, Lógicos e Controle de Fluxo** (==, !=, and, or, if, else, elif)
* **Laços de Repetição** (for, while, break, continue)
* **Formatação de Strings** (f-string)

<details>
<summary>Extra: Boas praticas (PEP8)</summary>

* Indentação
* Comprimento de Linha
* Nomes de variáveis
* Ferramentas de formatação (flake8, black, isort, pylint)

</details>

### 2. Estruturas de Dados Simples - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/02%20-%20Estruturas%20de%20Dados%20Simples)

* **Listas** (append, pop, index, slicing)
* **Tuplas** (imutabilidade, acesso por índice)
* **Dicionários** (keys, values, items, get)
* **Conjuntos (Sets)** (add, remove, union, intersection)
* **Manipulação e Métodos Comuns** (len, sorted)

<details>
<summary>Extra: Truques que deixam o codigo mais enxuto</summary>

* Desempacotamento de variaveis
* List, Dict e Set Comprehensions

</details>

### 3. Funções - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/03%20-%20Fun%C3%A7%C3%B5es)

* **Definição e Chamada de Funções** (def)
* **Parâmetros, Retorno e Escopo**
* **Funções Lambda**
* **Funções Recursivas**
* **Uso de Docstrings e Anotações de Tipo** (PEP 257, type hints)
* **Inner Functions** (funções aninhadas, escopo de funções)
* **Funções Built-in Simples** (len, sum, max, min)
* **Funções de Ordem Superior** (lambda, map, filter, any, all)
* **Funções de Iteráveis** (enumerate, reversed, zip)
* **Funções de Conversão** (int, float, str, bool)
* **Funções Especiais de Strings e Listas** (split, join, sorted, count)


### 4. Bibliotecas padrão - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o)

* **Importar Bibliotecas** (import, from)
* **random** (randint, choice, shuffle)
* **datetime** (now, strftime, timedelta)
* **math** (sqrt, ceil, floor, pi)
* **re** (search, findall, sub)

### 5. Manipulando Arquivos - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/05%20-%20Manipulando%20Arquivos)

* **Escrita e leitura de arquivos** (open, read, write, close, with)
* **Manipulação de Diretórios com `os`** (os.path, os.listdir, os.mkdir)
* **Arquivos Json** (json.load, json.dump)
* **Arquivos CSV** (csv.reader, csv.writer)
* **Arquivos binários** ('rb', 'wb', pickle)

## 🟡 **NÍVEL INTERMEDIÁRIO**

### 6. Programação Orientada a Objetos (POO) - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/06%20-%20Poo)

* **Classes e Objetos** (class, `__init__`, self)
* **Atributos e Métodos**
* **Métodos Estáticos e de Classe** (@staticmethod, @classmethod)
* **Herança e Polimorfismo** (super(), method overriding)
* **Encapsulamento** (público, protegido `_`, privado `__`)

### 7. Exceções e Erros - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/07%20-%20Exce%C3%A7%C3%B5es%20e%20Erros)

* **Tipos de Exceções Comuns** (TypeError, ValueError, IndexError, KeyError)
* **Tratamento de Erros** (try, except, else, finally)
* **Levantando Exceções Personalizadas** (raise, Exception)

### 8. Módulos e Pacotes - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/08%20-%20Modulos%20e%20pacotes)

* **Importação de Módulos próprios** (`__init__.py`)
* **Criação de Pacotes** (estrutura de diretórios)
* **Organização de Código** (separação de responsabilidades)
* **Introdução ao Gerenciamento de Dependências com `pip`** (requirements.txt, pip install)

### 9. Interface Gráfica com Tkinter - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/09%20-%20Interface%20Gr%C3%A1fica%20com%20Tkinter)

* **Estrutura básica de um programa com Tkinter** (Tk(), mainloop())
* **Widgets Básicos** (Label, Button, Entry, Text)
* **Layout e Organização** (pack, grid, place)
* **Manipulação de Eventos** (command, bind)

---

## 🔴 **NÍVEL AVANÇADO**

### 10. Funções avançadas e Iteração - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/10%20-%20Fun%C3%A7%C3%B5es%20avan%C3%A7adas%20e%20Itera%C3%A7%C3%A3o)

* **Decoradores** (@, wrapper, closure)
* **Iteradores** (`__iter__`, `__next__`, StopIteration)
* **Geradores** (yield, generator expression)

### 11. Gerenciamento de Dependências - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/11%20-%20Gerenciamento%20de%20Dependencias)

* **Virtualenv (pip + venv)** (python -m venv, source activate)
* **Poetry** (pyproject.toml, poetry install)
* **PDM** (pyproject.toml, pdm install)