# Estruturas de Dados Simples

---

## **Listas**

**1. Cadastro de Frutas**

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

**2. Inserindo em Posições Alternadas**

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

**3. Juntando Listas de Alunos**

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

**4. Removendo por Nome**

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

**5. Removendo pelo Índice**

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

**6. Contando Nomes Repetidos**

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

**7. Ordenando Números**

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

## **Tuplas**

**8. Criando e Acessando Tuplas**

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

---

**9. Encontrando Índices em Tuplas**

**Enunciado:** Crie uma tupla com números: `(10, 20, 30, 40, 50, 20)`. Peça ao usuário para digitar um número e use um método de tupla para mostrar o índice da primeira ocorrência desse número. Se o número não estiver na tupla, exiba uma mensagem informando.

**Objetivo:** Praticar o uso do método `index()` e tratamento de exceções simples.

**Requisitos de Conhecimento:**

* Tuplas
* Método `index()`
* Estruturas condicionais (`if`)

**Exemplo de Saída no Terminal:**

```
Digite um número: 20
O índice da primeira ocorrência é: 1
```

---

**10. Convertendo Lista em Tupla**

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

---

**11. Concatenando Tuplas**

**Enunciado:** Crie duas tuplas:

* `tupla1 = (1, 2, 3)`
* `tupla2 = (4, 5, 6)`
  Combine as duas tuplas em uma nova tupla chamada `tupla_completa` e exiba o resultado.

**Objetivo:** Treinar a concatenação de tuplas.

**Requisitos de Conhecimento:**

* Tuplas
* Operador `+`

**Exemplo de Saída no Terminal:**

```
Tupla completa: (1, 2, 3, 4, 5, 6)
```

---

**12. Repetindo Tuplas**

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

## **Dicionários**

**13. Criando um Dicionário**

**Enunciado:** Crie um dicionário chamado `aluno` com as chaves: `"nome"`, `"idade"` e `"curso"`. Peça ao usuário para digitar os valores correspondentes e preencha o dicionário. No final, exiba o dicionário completo.

**Objetivo:** Praticar a criação de dicionários e a atribuição de valores às chaves.

**Requisitos de Conhecimento:**

* Dicionários
* `input()`

**Exemplo de Saída no Terminal:**

```
Digite o nome do aluno: João
Digite a idade: 20
Digite o curso: Python
Dicionário do aluno: {'nome': 'João', 'idade': 20, 'curso': 'Python'}
```

---

**14. Acessando Valores**

**Enunciado:** Dado o dicionário:
`aluno = {"nome": "Ana", "idade": 22, "curso": "Java"}`
Peça ao usuário para digitar uma chave (`nome`, `idade` ou `curso`) e exiba o valor correspondente. Se a chave não existir, mostre uma mensagem informando.

**Objetivo:** Praticar o acesso a valores em dicionários e tratamento de chaves inexistentes.

**Requisitos de Conhecimento:**

* Dicionários
* `input()`
* Estruturas condicionais (`if`)

**Exemplo de Saída no Terminal:**

```
Digite a chave que deseja acessar: idade
O valor é: 22
```

---

**15. Atualizando Valores**

**Enunciado:** Crie um dicionário com informações de um produto:
`produto = {"nome": "Camiseta", "preco": 50, "quantidade": 10}`
Peça ao usuário para atualizar o preço e a quantidade do produto. No final, exiba o dicionário atualizado.

**Objetivo:** Praticar a atualização de valores em dicionários.

**Requisitos de Conhecimento:**

* Dicionários
* `input()`
* Conversão de tipos (`int()`, `float()`)

**Exemplo de Saída no Terminal:**

```
Digite o novo preço: 55
Digite a nova quantidade: 15
Produto atualizado: {'nome': 'Camiseta', 'preco': 55, 'quantidade': 15}
```

---

**16. Adicionando Novas Chaves**

**Enunciado:** Dado o dicionário do exercício anterior, peça ao usuário para adicionar uma nova chave `"cor"` com o valor desejado. Exiba o dicionário final.

**Objetivo:** Praticar a adição de novas chaves em dicionários existentes.

**Requisitos de Conhecimento:**

* Dicionários
* `input()`

**Exemplo de Saída no Terminal:**

```
Digite a cor do produto: azul
Produto final: {'nome': 'Camiseta', 'preco': 55, 'quantidade': 15, 'cor': 'azul'}
```

---

**17. Removendo Chaves**

**Enunciado:** Crie um dicionário com informações de uma pessoa:
`pessoa = {"nome": "Lucas", "idade": 28, "cidade": "São Paulo"}`
Peça ao usuário para digitar uma chave para remover. Se a chave existir, remova-a usando `pop()` e exiba o valor removido; caso contrário, mostre uma mensagem.

**Objetivo:** Praticar a remoção de chaves em dicionários com `pop()`.

**Requisitos de Conhecimento:**

* Dicionários
* Método `pop()`
* Estruturas condicionais

**Exemplo de Saída no Terminal:**

```
Digite a chave que deseja remover: cidade
Valor removido: São Paulo
Dicionário atualizado: {'nome': 'Lucas', 'idade': 28}
```

---

**18. Iterando sobre Dicionários**

**Enunciado:** Crie um dicionário com notas de alunos:
`notas = {"Ana": 8, "João": 7, "Maria": 9}`
Use um laço `for` para imprimir cada aluno e sua nota no formato: `"Aluno: <nome>, Nota: <nota>"`.

**Objetivo:** Praticar a iteração sobre chaves e valores de um dicionário usando `items()`.

**Requisitos de Conhecimento:**

* Dicionários
* Laço `for`
* Método `items()`

**Exemplo de Saída no Terminal:**

```
Aluno: Ana, Nota: 8
Aluno: João, Nota: 7
Aluno: Maria, Nota: 9
```

---

## **Conjuntos (Sets)**

**19. Criando um Conjunto**

**Enunciado:** Crie um conjunto vazio chamado `numeros`. Peça ao usuário para digitar 5 números (um por vez) e adicione-os ao conjunto usando `add()`. No final, exiba o conjunto.

**Objetivo:** Praticar a criação de conjuntos e a inserção de elementos usando `add()`.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Laço `for`
* `input()` e conversão para inteiro (`int()`)

**Exemplo de Saída no Terminal:**

```
Digite um número: 5
Digite um número: 3
Digite um número: 5
Digite um número: 8
Digite um número: 2
Conjunto final: {2, 3, 5, 8}
```

---

**20. Removendo Elementos**

**Enunciado:** Dado o conjunto `numeros = {1, 2, 3, 4, 5}`, peça ao usuário para digitar um número a ser removido. Se o número existir, remova-o usando `discard()`. Caso não exista, exiba uma mensagem informando.

**Objetivo:** Praticar a remoção de elementos em conjuntos usando `discard()`.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `discard()`
* `input()` e conversão para inteiro (`int()`)

**Exemplo de Saída no Terminal:**

```
Digite um número para remover: 3
Conjunto atualizado: {1, 2, 4, 5}
```

---

**21. Verificando Pertinência**

**Enunciado:** Crie um conjunto `cores = {"vermelho", "azul", "verde"}`. Peça ao usuário para digitar uma cor e verifique se ela está no conjunto. Exiba uma mensagem informando se a cor está presente ou não.

**Objetivo:** Praticar a verificação de existência de elementos em conjuntos usando o operador `in`.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Operador `in`
* `input()`

**Exemplo de Saída no Terminal:**

```
Digite uma cor: azul
A cor azul está no conjunto.
```

---

**22. União de Conjuntos**

**Enunciado:** Crie dois conjuntos:
`conjunto1 = {1, 2, 3}`
`conjunto2 = {3, 4, 5}`
Crie um novo conjunto que seja a união dos dois conjuntos usando `union()` e exiba o resultado.

**Objetivo:** Praticar a união de conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `union()` ou operador `|`

**Exemplo de Saída no Terminal:**

```
Conjunto união: {1, 2, 3, 4, 5}
```

---

**23. Interseção de Conjuntos**

**Enunciado:** Crie dois conjuntos:
`conjunto1 = {"maçã", "banana", "laranja"}`
`conjunto2 = {"banana", "uva", "laranja"}`
Crie um novo conjunto com os elementos presentes em ambos os conjuntos usando `intersection()`.

**Objetivo:** Praticar a interseção de conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `intersection()` ou operador `&`

**Exemplo de Saída no Terminal:**

```
Conjunto interseção: {'banana', 'laranja'}
```

---

**24. Diferença entre Conjuntos**

**Enunciado:** Dado:
`conjunto1 = {1, 2, 3, 4}`
`conjunto2 = {3, 4, 5, 6}`
Crie um conjunto que contenha apenas os elementos que estão em `conjunto1` mas não em `conjunto2` usando `difference()`.

**Objetivo:** Praticar a diferença entre conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `difference()` ou operador `-`

**Exemplo de Saída no Terminal:**

```
Diferença: {1, 2}
```

---

**25. Subconjuntos e Superconjuntos**

**Enunciado:** Crie dois conjuntos:
`A = {1, 2, 3}`
`B = {1, 2, 3, 4, 5}`
Verifique se `A` é um subconjunto de `B` e se `B` é um superconjunto de `A`. Exiba mensagens correspondentes.

**Objetivo:** Praticar os métodos `issubset()` e `issuperset()` para verificar relações entre conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Métodos `issubset()` e `issuperset()`

**Exemplo de Saída no Terminal:**

```
A é subconjunto de B? True
B é superconjunto de A? True
```




