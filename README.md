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

* **O que é Python e sua Filosofia** - [Documentário](https://youtu.be/GfH4QL4VqJ0)
* **Instalação do Python** - [Download](https://www.python.org/downloads/)
* **Uso do VS Code** - [Download](https://code.visualstudio.com/)
* **Shell interativo vs script** *(python3, arquivo.py)*

## 🟢 **NÍVEL BÁSICO**

### 1. Sintaxe Básica - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/01%20-%20Sintaxe%20B%C3%A1sica)

* **Saida de dados**
* **Variáveis, tipos e conversão de tipos**
* **Entrada de dados**
* **Operadores Aritméticos**
* **Operadores Relacionais, Lógicos e Controle de Fluxo**
* **Laços de Repetição**
* **Formatação de Strings**

<details>
<summary>Extra: Boas praticas (PEP8)</summary>

* Indentação
* Comprimento de Linha
* Nomes de variáveis
* Ferramentas de formatação (flake8, black, isort, pylint)

</details>

### 2. Estruturas de Dados Simples

* **Listas** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/02%20-%20Estruturas%20de%20Dados%20Simples/01%20-%20Listas)**
* **Tuplas** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/02%20-%20Estruturas%20de%20Dados%20Simples/02%20-%20Tuplas)**
* **Dicionários** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/02%20-%20Estruturas%20de%20Dados%20Simples/03%20-%20Dicionarios)**
* **Conjuntos (Sets)** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/02%20-%20Estruturas%20de%20Dados%20Simples/04%20-%20Conjuntos%20(Sets))**

<details>
<summary>Extra: Truques que deixam o codigo mais enxuto</summary>

* Desempacotamento de variaveis
* List, Dict e Set Comprehensions

</details>

### 3. Funções - [Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/03%20-%20Fun%C3%A7%C3%B5es)

* **Definição e Chamada de Funções**
* **Parâmetros, Retorno e Escopo**
* **Funções Lambda**
* **Funções Recursivas**
* **Uso de Docstrings e Anotações de Tipo**
* **Inner Functions**
* **Funções Built-in Simples**
* **Funções de Ordem Superior**
* **Funções de Iteráveis**
* **Funções de Conversão**
* **Funções Especiais de Strings e Listas**

### 4. Bibliotecas built-in

* **random** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o/01%20-%20Random)**
* **datetime** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/blob/main/04%20-%20Bibliotecas%20Padr%C3%A3o/02%20-%20DateTime)**
* **math** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o/03%20-%20Math)**
* **os** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o/04%20-%20Os)**
* **sys** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o/05%20-%20Sys)**
* **re** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/04%20-%20Bibliotecas%20Padr%C3%A3o/06%20-%20Re(Express%C3%B5es%20Regulares))**

### 5. Manipulando Arquivos

* **Escrita e leitura de arquivos** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/05%20-%20Manipulando%20Arquivos/01%20-%20Escrita%20e%20leitura%20de%20arquivos)**
* **Arquivos Json** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/05%20-%20Manipulando%20Arquivos/02%20-%20Arquivo%20Json)**
* **Arquivos CSV** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/05%20-%20Manipulando%20Arquivos/03%20-%20Arquivo%20csv)**
* **Arquivos binários** - **[Exercícios](https://github.com/Ricardo7c/Python-Roadmap/tree/main/05%20-%20Manipulando%20Arquivos/04%20-%20Arquivo%20Binario)**

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

🛠 **Projetos Práticos**
------------------------

Com os conhecimentos adquiridos até aqui, você já é capaz de desenvolver pequenos projetos para consolidar sua base em Python.  
Esses exercícios práticos são um passo importante antes de seguir para os conteúdos avançados.

1. **[Calculadora (CLI)](https://github.com/Ricardo7c/Python-Roadmap/tree/main/Projetos/1%20-%20Calculadora(CLI))**
   
   * Projeto em linha de comando para reforçar **funções, operadores e tratamento de erros**.

2. **[Jogo da Forca (CLI)](https://github.com/Ricardo7c/Python-Roadmap/tree/main/Projetos/2%20-%20Jogo%20da%20forca(CLI))**
   
   * Aplicação no terminal utilizando **laços, manipulação de strings e arquivos**, além de lógica condicional.

3. **[Jogo da Velha (GUI)](https://github.com/Ricardo7c/Python-Roadmap/tree/main/Projetos/3%20-%20Jogo%20da%20velha(GUI))**
   
   * Versão gráfica com Tkinter, explorando **widgets, eventos e organização de layout**.

4. **[Calculadora (GUI)](https://github.com/Ricardo7c/Python-Roadmap/tree/main/Projetos/4%20-%20Calculadora%20(GUI))**
   
   * Calculadora com interface Tkinter para praticar **POO, eventos e componentes gráficos**.
     
     

📌 **Objetivo**: aplicar de forma prática o que você aprendeu, transformando teoria em projetos reais.

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
