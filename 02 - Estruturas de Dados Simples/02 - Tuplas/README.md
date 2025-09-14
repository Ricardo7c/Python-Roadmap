# **Tuplas**

**01. Criando e Acessando Tuplas**

**Enunciado:** Crie uma tupla chamada `cores` contendo cinco cores diferentes. Peça ao usuário para digitar um número entre 0 e 4 e exiba a cor correspondente ao índice digitado.

**Objetivo:** Praticar a criação de tuplas e o acesso a elementos usando índices.

**Requisitos de Conhecimento:**

* Tuplas
* Índices
* `input()` e conversão de tipos (`int()`)

**Exemplo de Saída no Terminal:**

    Digite um índice (0-4): 2
    A cor selecionada é: verde

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

    Digite uma fruta: maçã
    Digite uma fruta: banana
    Digite uma fruta: uva
    Digite uma fruta: manga
    Digite uma fruta: abacaxi
    Tupla final: ('maçã', 'banana', 'uva', 'manga', 'abacaxi')

**04. Concatenando Tuplas**

**Enunciado:** Crie duas tuplas:

* `tupla1 = (1, 2, 3)`
* `tupla2 = (4, 5, 6)`Combine as duas tuplas em uma nova tupla chamada `tupla_completa` e exiba o resultado.

**Objetivo:** Treinar a concatenação de tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Operador `+`

**Exemplo de Saída no Terminal:**

    Tupla completa: (1, 2, 3, 4, 5, 6)

**05. Repetindo Tuplas**

**Enunciado:** Crie uma tupla `numeros = (7, 8, 9)`. Peça ao usuário para digitar um número inteiro `n` e crie uma nova tupla que repita `numeros` `n` vezes.

**Objetivo:** Praticar a multiplicação de tuplas para criar repetições.

**Requisitos de Conhecimento:**

* Tuplas
* Operador `*`
* `input()` e conversão para inteiro

**Exemplo de Saída no Terminal:**

    Digite um número: 3
    Nova tupla: (7, 8, 9, 7, 8, 9, 7, 8, 9)