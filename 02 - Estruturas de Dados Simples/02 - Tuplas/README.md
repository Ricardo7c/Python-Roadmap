# **Tuplas**

**01. Criando e Acessando Tuplas**

**Enunciado:** Crie uma tupla chamada `cores` contendo cinco cores diferentes. Peça ao usuário para digitar um número entre 0 e 4 e exiba a cor correspondente ao índice digitado.

**Objetivo:** Praticar a criação de tuplas e o acesso a elementos usando índices.

**Requisitos de Conhecimento:**

* Tuplas
* Índices
* `input()` e conversão de tipos (`int()`)

**Exemplo de Saída no Terminal:**

```
Digite um índice (0-4): 2
A cor selecionada é: verde
```

**02. Encontrando Índices em Tuplas**

**Enunciado:** Crie uma tupla com números: `(10, 20, 30, 40, 50, 20)`. Peça ao usuário para digitar um número e use um método de tupla para mostrar o índice da primeira ocorrência desse número. Se o número não estiver na tupla, exiba uma mensagem informando.

**Objetivo:** Praticar o uso do método `index()` e tratamento de exceções simples.

**Requisitos de Conhecimento:**

* Tuplas
* Método `index()`
* Estruturas condicionais (`if`)

**Exemplo de Saída no Terminal:**

    Digite um número: 20
    O índice da primeira ocorrência é: 1

**03. Convertendo Lista em Tupla**

**Enunciado:** Peça ao usuário para digitar 5 frutas e armazene-as em uma lista. Depois, converta a lista em uma tupla e exiba a tupla final.

**Objetivo:** Praticar a conversão entre listas e tuplas.

**Requisitos de Conhecimento:**

* Listas
* Tuplas
* `for`
* `tuple()`

**Exemplo de Saída no Terminal:**
```
Digite uma fruta: maçã
Digite uma fruta: banana
Digite uma fruta: uva
Digite uma fruta: manga
Digite uma fruta: abacaxi
Tupla final: ('maçã', 'banana', 'uva', 'manga', 'abacaxi')
```

**04. Concatenando Tuplas**

**Enunciado:** Crie duas tuplas:

* `tupla1 = (1, 2, 3)`
* `tupla2 = (4, 5, 6)`Combine as duas tuplas em uma nova tupla chamada `tupla_completa` e exiba o resultado.

**Objetivo:** Treinar a concatenação de tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Operador `+`

**Exemplo de Saída no Terminal:**

```
Tupla completa: (1, 2, 3, 4, 5, 6)
```

**05. Repetindo Tuplas**

**Enunciado:** Crie uma tupla `numeros = (7, 8, 9)`. Peça ao usuário para digitar um número inteiro `n` e crie uma nova tupla que repita `numeros` `n` vezes.

**Objetivo:** Praticar a multiplicação de tuplas para criar repetições.

**Requisitos de Conhecimento:**

* Tuplas
* Operador `*`
* `input()` e conversão para inteiro

**Exemplo de Saída no Terminal:**
```
Digite um número: 3
Nova tupla: (7, 8, 9, 7, 8, 9, 7, 8, 9)
```

---

**06. Contando Elementos em Tuplas**

**Enunciado:** Crie uma tupla `numeros = (1, 2, 3, 2, 4, 2, 5)`. Peça ao usuário para digitar um número e use o método `count()` para mostrar quantas vezes ele aparece na tupla.

**Objetivo:** Praticar o método `count()` em tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Método `count()`
* `input()`

**Exemplo de Saída no Terminal:**

```
Digite um número: 2
O número aparece 3 vezes na tupla.
```

---

**07. Tamanho da Tupla**

**Enunciado:** Crie uma tupla com nomes de animais. Exiba todos os elementos da tupla e o tamanho dela usando `len()`.

**Objetivo:** Praticar o uso de `len()` em tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Função `len()`

**Exemplo de Saída no Terminal:**

```
Tupla de animais: ('gato', 'cachorro', 'pássaro', 'peixe')
Tamanho da tupla: 4
```

---

**08. Desempacotando Tuplas**

**Enunciado:** Crie uma tupla `pessoa = ("Carlos", 25, "Engenheiro")`. Use desempacotamento de variáveis para armazenar cada elemento em variáveis separadas (`nome`, `idade`, `profissao`) e exiba uma mensagem formatada com essas informações.

**Objetivo:** Treinar o desempacotamento de tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Desempacotamento de variáveis

**Exemplo de Saída no Terminal:**

```
Nome: Carlos, Idade: 25, Profissão: Engenheiro
```

---

**09. Iterando sobre Tuplas**

**Enunciado:** Crie uma tupla `cores = ("vermelho", "azul", "verde", "amarelo")`. Use um laço `for` para exibir cada cor da tupla.

**Objetivo:** Praticar iteração sobre tuplas com `for`.

**Requisitos de Conhecimento:**

* Tuplas
* Laço `for`

**Exemplo de Saída no Terminal:**

```
Cor: vermelho
Cor: azul
Cor: verde
Cor: amarelo
```

---

**10. Tuplas como Coordenadas**

**Enunciado:** Crie uma tupla `ponto = (10, 20)`. Exiba a posição no plano cartesiano no formato `(x, y)`. Depois, crie outra tupla `ponto2 = (30, 40)` e mostre os dois pontos juntos dentro de uma lista.

**Objetivo:** Mostrar o uso de tuplas para representar dados imutáveis como coordenadas.

**Requisitos de Conhecimento:**

* Tuplas
* Listas

**Exemplo de Saída no Terminal:**

```
Ponto 1: (10, 20)
Ponto 2: (30, 40)
Lista de pontos: [(10, 20), (30, 40)]
```

---
