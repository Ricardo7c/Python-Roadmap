# Modulos e Pacotes

## 1. Módulos Próprios

**Objetivo:** Criar e importar um módulo próprio.  

1. Crie um arquivo chamado `utils.py`.  
2. Neste arquivo, defina as seguintes funções:  
   - `soma(a, b)` - Retorna a soma de dois números.  
   - `subtracao(a, b)` - Retorna a subtração de dois números.  
3. Crie outro script chamado `main.py` que importe e utilize as funções do módulo `utils`.  

---

## 2. Criação de Pacotes

**Objetivo:** Organizar o código em pacotes.  

1. Crie uma estrutura de diretórios como esta:  

   ```powershell
   calculadora/
       __init__.py
       operacoes/
           __init__.py
           basicas.py
           avancadas.py
   ```

2. No arquivo `basicas.py`, implemente as funções `adicao(a, b)` e `multiplicacao(a, b)`.  
3. No arquivo `avancadas.py`, implemente as funções `potencia(base, expoente)` e `raiz_quadrada(numero)`.  
4. Crie um script principal (`main.py`) fora do pacote que importe as funções e permita ao usuário executar as operações.  

---

## 3. Introdução ao pip

**Objetivo:** Instalar e usar pacotes externos.  

1. Instale o pacote `requests` usando o pip.  
2. Crie um script chamado `seguidores.py` que:  
   - Use o pacote `requests` para obter dados da api publica do github: (`https://api.github.com`)
   - Solicite um nome de usuario do github e mostre seus seguidores

---
