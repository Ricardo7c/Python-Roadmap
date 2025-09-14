# **Dicionários**

**01. Criando um Dicionário**

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

**02. Acessando Valores**

**Enunciado:** Dado o dicionário:`aluno = {"nome": "Ana", "idade": 22, "curso": "Java"}`Peça ao usuário para digitar uma chave (`nome`, `idade` ou `curso`) e exiba o valor correspondente. Se a chave não existir, mostre uma mensagem informando.

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

**03. Atualizando Valores**

**Enunciado:** Crie um dicionário com informações de um produto:`produto = {"nome": "Camiseta", "preco": 50, "quantidade": 10}`Peça ao usuário para atualizar o preço e a quantidade do produto. No final, exiba o dicionário atualizado.

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

**04. Adicionando Novas Chaves**

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

**05. Removendo Chaves**

**Enunciado:** Crie um dicionário com informações de uma pessoa:`pessoa = {"nome": "Lucas", "idade": 28, "cidade": "São Paulo"}`Peça ao usuário para digitar uma chave para remover. Se a chave existir, remova-a usando `pop()` e exiba o valor removido; caso contrário, mostre uma mensagem.

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

**06. Iterando sobre Dicionários**

**Enunciado:** Crie um dicionário com notas de alunos:`notas = {"Ana": 8, "João": 7, "Maria": 9}`Use um laço `for` para imprimir cada aluno e sua nota no formato: `"Aluno: <nome>, Nota: <nota>"`.

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

### 07. Usando `get()` para Acessar Valores

**Enunciado:** Crie um dicionário chamado `capital` com algumas chaves de países e valores correspondentes às suas capitais. Peça ao usuário para digitar um país e exiba a capital usando o método `get()`. Se o país não existir no dicionário, exiba `"País não encontrado"`.

**Objetivo:** Praticar o acesso seguro a valores em dicionários usando `get()`.

**Requisitos de Conhecimento:**

* Dicionários
* Método `get()`
* `input()`

**Exemplo de Saída no Terminal:**

```
Digite o país: Brasil
A capital é: Brasília
```

### 08. Listando Apenas as Chaves

**Enunciado:** Dado o dicionário `aluno = {"nome": "Carla", "idade": 21, "curso": "Python"}`, use o método `keys()` para exibir todas as chaves do dicionário.

**Objetivo:** Praticar o uso do método `keys()` para obter apenas as chaves de um dicionário.

**Requisitos de Conhecimento:**

* Dicionários
* Método `keys()`

**Exemplo de Saída no Terminal:**

```
Chaves do dicionário: dict_keys(['nome', 'idade', 'curso'])
```

### 09. Listando Apenas os Valores

**Enunciado:** Dado o mesmo dicionário do exercício anterior, utilize o método `values()` para exibir apenas os valores.

**Objetivo:** Treinar o uso do método `values()`.

**Requisitos de Conhecimento:**

* Dicionários
* Método `values()`

**Exemplo de Saída no Terminal:**

```
Valores do dicionário: dict_values(['Carla', 21, 'Python'])
```

### 10. Mesclando Dicionários com `update()`

**Enunciado:** Crie dois dicionários:

```
dados1 = {"nome": "Carlos", "idade": 30}  
dados2 = {"curso": "Python", "cidade": "Recife"}  
```

Use o método `update()` para mesclar `dados2` dentro de `dados1`. Exiba o dicionário final.

**Objetivo:** Praticar a fusão de dicionários com `update()`.

**Requisitos de Conhecimento:**

* Dicionários
* Método `update()`

**Exemplo de Saída no Terminal:**

```
Dicionário final: {'nome': 'Carlos', 'idade': 30, 'curso': 'Python', 'cidade': 'Recife'}
```

### 11. Copiando Dicionários

**Enunciado:** Crie um dicionário `original = {"a": 1, "b": 2, "c": 3}`. Faça uma cópia usando o método `copy()`.
Modifique a cópia adicionando uma nova chave `"d": 4` e exiba os dois dicionários para mostrar que são independentes.

**Objetivo:** Entender a diferença entre referências e cópias de dicionários.

**Requisitos de Conhecimento:**

* Dicionários
* Método `copy()`

**Exemplo de Saída no Terminal:**

```
Original: {'a': 1, 'b': 2, 'c': 3}
Cópia: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### 12. Limpando um Dicionário

**Enunciado:** Crie um dicionário `dados = {"x": 10, "y": 20, "z": 30}`. Use o método `clear()` para remover todos os itens e exiba o dicionário vazio.

**Objetivo:** Praticar o uso do método `clear()` para limpar um dicionário.

**Requisitos de Conhecimento:**

* Dicionários
* Método `clear()`

**Exemplo de Saída no Terminal:**

```
Dicionário após clear(): {}
```