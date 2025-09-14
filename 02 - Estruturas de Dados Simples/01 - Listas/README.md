# **Listas**

**01. Cadastro de Frutas**

**Enunciado:** Crie uma lista vazia chamada `frutas`. Use um laço `for` para pedir que o usuário digite 5 frutas e adicione cada uma delas na lista usando `append()`. No final, exiba todas as frutas cadastradas.

**Objetivo:** Praticar o uso de `append()` junto com `for` para inserir vários elementos em uma lista.

**Requisitos de Conhecimento:**

* `for`
* `input()`
* Listas
* Método `append()`

**Exemplo de Saída no Terminal:**

```
Digite uma fruta: maçã
Digite uma fruta: banana
Digite uma fruta: uva
Digite uma fruta: manga
Digite uma fruta: abacaxi
Lista de frutas: ['maçã', 'banana', 'uva', 'manga', 'abacaxi']
```

---

**02. Inserindo em Posições Alternadas**

**Enunciado:** Crie uma lista inicial `[100, 200, 300, 400, 500]`. Peça ao usuário 3 números. Use um laço `for` para inserir cada número sempre na posição 1 da lista com `insert()`.

**Objetivo:** Treinar `insert()` dentro de um laço para manipular posições fixas.

**Requisitos de Conhecimento:**

* `for`
* Listas
* Método `insert()`

**Exemplo de Saída no Terminal:**

```
Digite um número: 50
Digite um número: 60
Digite um número: 70
Lista final: [100, 70, 60, 50, 200, 300, 400, 500]
```

---

**03. Juntando Listas de Alunos**

**Enunciado:** Crie duas listas:

* `turma1` deve receber 3 nomes digitados pelo usuário.
* `turma2` deve receber 2 nomes digitados pelo usuário.
  Use `extend()` para juntar as duas listas em uma só chamada `turma_completa`.

**Objetivo:** Praticar laços de repetição para preencher listas e depois uni-las com `extend()`.

**Requisitos de Conhecimento:**

* `for`
* Listas
* Método `extend()`

**Exemplo de Saída no Terminal:**

```
Digite um aluno da turma 1: Ana
Digite um aluno da turma 1: João
Digite um aluno da turma 1: Pedro
Digite um aluno da turma 2: Maria
Digite um aluno da turma 2: Lucas
Turma completa: ['Ana', 'João', 'Pedro', 'Maria', 'Lucas']
```

---

**04. Removendo por Nome**

**Enunciado:** Crie uma lista inicial com 5 cores. Peça ao usuário para digitar uma cor repetidamente até que ele digite `"sair"`. Sempre que a cor existir na lista, remova usando `remove()`. No final, exiba a lista atualizada.

**Objetivo:** Treinar `remove()` junto com laços `while`.

**Requisitos de Conhecimento:**

* `while`
* `input()`
* Listas
* Método `remove()`

**Exemplo de Saída no Terminal:**

```
Digite uma cor para remover (ou 'sair' para encerrar): azul
Digite uma cor para remover (ou 'sair' para encerrar): verde
Digite uma cor para remover (ou 'sair' para encerrar): sair
Lista final: ['vermelho', 'amarelo', 'preto']
```

---

**05. Removendo pelo Índice**

**Enunciado:** Crie uma lista com os números `[10, 20, 30, 40, 50]`. Use um laço `while` para remover elementos da lista com `pop()` até que ela fique vazia, mostrando sempre o número removido.

**Objetivo:** Treinar `pop()` em conjunto com laços até esvaziar a lista.

**Requisitos de Conhecimento:**

* `while`
* Listas
* Método `pop()`

**Exemplo de Saída no Terminal:**

```
Número removido: 50
Número removido: 40
Número removido: 30
Número removido: 20
Número removido: 10
Lista final: []
```

---

**06. Contando Nomes Repetidos**

**Enunciado:** Peça ao usuário para digitar 5 nomes (usando `for`). Depois, pergunte um nome específico e mostre quantas vezes ele aparece na lista usando `count()`.

**Objetivo:** Treinar `count()` em listas preenchidas dinamicamente.

**Requisitos de Conhecimento:**

* `for`
* Listas
* Método `count()`

**Exemplo de Saída no Terminal:**

```
Digite um nome: Ana
Digite um nome: João
Digite um nome: Ana
Digite um nome: Pedro
Digite um nome: Ana
Digite um nome para contar: Ana
O nome aparece 3 vezes na lista.
```

---

**07. Ordenando Números**

**Enunciado:** Peça ao usuário para digitar 7 números e armazene-os em uma lista. Use `sort()` para ordenar em ordem crescente e `reverse()` para inverter a ordem.

**Objetivo:** Treinar `sort()` e `reverse()` em listas criadas por entrada do usuário.

**Requisitos de Conhecimento:**

* `for`
* Listas
* Métodos `sort()` e `reverse()`

**Exemplo de Saída no Terminal:**

```
Digite um número: 42
Digite um número: 7
Digite um número: 15
Digite um número: 3
Digite um número: 27
Digite um número: 100
Digite um número: 1
Lista em ordem crescente: [1, 3, 7, 15, 27, 42, 100]
Lista invertida: [100, 42, 27, 15, 7, 3, 1]
```
---

**08. Encontrando o Índice de um Elemento**

**Enunciado:** Crie uma lista com nomes de cidades: `["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]`. Peça ao usuário para digitar o nome de uma cidade e use `index()` para mostrar a posição dela na lista. Caso a cidade não exista, exiba uma mensagem.

**Objetivo:** Treinar o método `index()` para localizar elementos em listas.

**Requisitos de Conhecimento:**

* Listas
* Método `index()`
* Estruturas condicionais

**Exemplo de Saída no Terminal:**

```
Digite o nome da cidade: Curitiba
A cidade está na posição 3
```

---

**09. Copiando Listas**

**Enunciado:** Crie uma lista `original = [1, 2, 3, 4, 5]`. Faça uma cópia com `copy()` e adicione o número 6 apenas na cópia. Exiba as duas listas para mostrar que são independentes.

**Objetivo:** Entender a diferença entre referência e cópia de listas.

**Requisitos de Conhecimento:**

* Listas
* Método `copy()`

**Exemplo de Saída no Terminal:**

```
Original: [1, 2, 3, 4, 5]
Cópia: [1, 2, 3, 4, 5, 6]
```

---

**10. Limpando a Lista**

**Enunciado:** Crie uma lista `dados = [10, 20, 30, 40]`. Use o método `clear()` para esvaziá-la. Exiba a lista final.

**Objetivo:** Treinar o método `clear()` para remover todos os elementos de uma lista.

**Requisitos de Conhecimento:**

* Listas
* Método `clear()`

**Exemplo de Saída no Terminal:**

```
Lista final: []
```

---

**11. Tamanho da Lista**

**Enunciado:** Peça ao usuário para digitar números até que ele digite `0`. Armazene-os em uma lista e, ao final, exiba a lista completa e o total de elementos usando `len()`.

**Objetivo:** Praticar o uso de `len()` para obter o tamanho de uma lista.

**Requisitos de Conhecimento:**

* `while`
* Listas
* Função `len()`

**Exemplo de Saída no Terminal:**

```
Digite um número (0 para parar): 5
Digite um número (0 para parar): 10
Digite um número (0 para parar): 15
Digite um número (0 para parar): 0
Lista: [5, 10, 15]
Total de elementos: 3
```

---