# **Conjuntos (Sets)**

**01. Criando um Conjunto**

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

**02. Removendo Elementos**

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

**03. Verificando Pertinência**

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

**04. União de Conjuntos**

**Enunciado:** Crie dois conjuntos:`conjunto1 = {1, 2, 3}``conjunto2 = {3, 4, 5}`Crie um novo conjunto que seja a união dos dois conjuntos usando `union()` e exiba o resultado.

**Objetivo:** Praticar a união de conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `union()` ou operador `|`

**Exemplo de Saída no Terminal:**
```
Conjunto união: {1, 2, 3, 4, 5}
```

**05. Interseção de Conjuntos**

**Enunciado:** Crie dois conjuntos:`conjunto1 = {"maçã", "banana", "laranja"}``conjunto2 = {"banana", "uva", "laranja"}`Crie um novo conjunto com os elementos presentes em ambos os conjuntos usando `intersection()`.

**Objetivo:** Praticar a interseção de conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `intersection()` ou operador `&`

**Exemplo de Saída no Terminal:**
```
Conjunto interseção: {'banana', 'laranja'}
```

**06. Diferença entre Conjuntos**

**Enunciado:** Dado:`conjunto1 = {1, 2, 3, 4}``conjunto2 = {3, 4, 5, 6}`Crie um conjunto que contenha apenas os elementos que estão em `conjunto1` mas não em `conjunto2` usando `difference()`.

**Objetivo:** Praticar a diferença entre conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `difference()` ou operador `-`

**Exemplo de Saída no Terminal:**
```
Diferença: {1, 2}
```

**07. Subconjuntos e Superconjuntos**

**Enunciado:** Crie dois conjuntos:`A = {1, 2, 3}``B = {1, 2, 3, 4, 5}`Verifique se `A` é um subconjunto de `B` e se `B` é um superconjunto de `A`. Exiba mensagens correspondentes.

**Objetivo:** Praticar os métodos `issubset()` e `issuperset()` para verificar relações entre conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Métodos `issubset()` e `issuperset()`

**Exemplo de Saída no Terminal:**
```
A é subconjunto de B? True
B é superconjunto de A? True
```
---

**08. Diferença Simétrica**

**Enunciado:** Crie dois conjuntos:

```
A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}  
```

Use o método `symmetric_difference()` para criar um novo conjunto com os elementos que estão em apenas um dos conjuntos (mas não em ambos).

**Objetivo:** Praticar o uso de `symmetric_difference()` em conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `symmetric_difference()` ou operador `^`

**Exemplo de Saída no Terminal:**

```
Diferença simétrica: {1, 2, 5, 6}
```

---

**09. Copiando Conjuntos**

**Enunciado:** Crie um conjunto `numeros = {10, 20, 30}`. Faça uma cópia usando `copy()` e adicione o número `40` apenas na cópia. Exiba os dois conjuntos para mostrar que são independentes.

**Objetivo:** Entender a diferença entre referência e cópia em conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `copy()`

**Exemplo de Saída no Terminal:**

```
Conjunto original: {10, 20, 30}
Cópia modificada: {10, 20, 30, 40}
```

---

**10. Limpando um Conjunto**

**Enunciado:** Crie um conjunto `dados = {1, 2, 3, 4, 5}`. Use o método `clear()` para remover todos os elementos e exiba o conjunto vazio.

**Objetivo:** Praticar o uso de `clear()` em conjuntos.

**Requisitos de Conhecimento:**

* Conjuntos (`set`)
* Método `clear()`

**Exemplo de Saída no Terminal:**

```
Conjunto após clear(): set()
```

---

**11. Removendo Duplicados de uma Lista**

**Enunciado:** Peça ao usuário para digitar 7 números e armazene-os em uma lista. Converta a lista em um conjunto para remover os duplicados e exiba o conjunto final.

**Objetivo:** Mostrar como conjuntos podem ser usados para eliminar elementos repetidos.

**Requisitos de Conhecimento:**

* Listas
* Conjuntos (`set()`)
* Conversão de tipos

**Exemplo de Saída no Terminal:**

```
Digite um número: 5
Digite um número: 3
Digite um número: 5
Digite um número: 7
Digite um número: 3
Digite um número: 9
Digite um número: 1
Conjunto sem duplicados: {1, 3, 5, 7, 9}
```

---
