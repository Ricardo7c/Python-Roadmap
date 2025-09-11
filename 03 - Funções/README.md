# Funções em Python

## Definição e Chamada de Funções
. Boas-vindas**

**Enunciado:** Crie uma função chamada `exibir_boas_vindas` que exibe a mensagem `"Bem-vindo ao curso de Python!"` quando chamada. Chame essa função no programa principal.

**Objetivo:** Praticar a definição e chamada de funções simples.

**Exemplo de saída no terminal:**

```
Bem-vindo ao curso de Python!
```
---

**2. Mostrar número**

**Enunciado:** Implemente uma função chamada `mostrar_numero` que recebe um número inteiro como parâmetro e exibe: `"O número informado foi: {numero}"`. Teste a função passando diferentes valores.

**Objetivo:** Praticar passagem de parâmetros para funções.

**Exemplo de saída no terminal:**

```
O número informado foi: 10
O número informado foi: 25
```
---

**3. Soma de dois números**

**Enunciado:** Escreva uma função chamada `calcular_soma` que recebe dois números como parâmetros, calcula a soma deles e exibe o resultado.

**Objetivo:** Praticar funções com múltiplos parâmetros.

**Exemplo de saída no terminal:**

```
A soma de 5 e 7 é 12
A soma de 10 e 20 é 30
```

---

## Parâmetros e Retorno

**4. Área do retângulo**

**Enunciado:** Implemente uma função chamada `calcular_area_retangulo` que recebe a largura e a altura de um retângulo como parâmetros e retorna sua área.

**Objetivo:** Praticar retorno de valores em funções.

**Exemplo de saída no terminal:**

```
Área do retângulo: 20
```
---

**5. Verificar paridade**

**Enunciado:** Escreva uma função chamada `verificar_paridade` que recebe um número inteiro e retorna `"Par"` ou `"Ímpar"`.

**Objetivo:** Praticar lógica condicional e retorno de strings.

**Exemplo de saída no terminal:**

```
Número 4 é Par
Número 7 é Ímpar
```
---

**6. Potência de um número**

**Enunciado:** Crie uma função chamada `calcular_potencia` que recebe dois números: base e expoente, e retorna o resultado da base elevada ao expoente.

**Objetivo:** Treinar operações matemáticas e retorno de valores.

**Exemplo de saída no terminal:**

```
2 elevado a 3 é 8
5 elevado a 2 é 25
```

---

## Funções Lambda

**7. Maior de dois números**

**Enunciado:** Escreva uma função lambda que recebe dois números e retorna o maior deles. Use a função lambda com diferentes pares de números.

**Objetivo:** Praticar funções anônimas.

**Exemplo de saída no terminal:**

```
Maior entre 3 e 7 é 7
Maior entre 10 e 5 é 10
```
---

**8. Quadrado de números**

**Enunciado:** Crie uma lista de números e use uma função lambda com o método `map` para calcular o quadrado de cada número na lista. Exiba a lista original e a transformada.

**Objetivo:** Treinar funções lambda e uso de `map`.

**Exemplo de saída no terminal:**

```
Lista original: [1, 2, 3, 4]
Lista ao quadrado: [1, 4, 9, 16]
```
---

**9. Filtrar divisíveis por 3**

**Enunciado:** Implemente uma função lambda que recebe um número e verifica se ele é divisível por 3. Use essa função com `filter` para filtrar os números divisíveis por 3 de uma lista.

**Objetivo:** Praticar funções lambda e `filter`.

**Exemplo de saída no terminal:**

```
Números divisíveis por 3: [3, 6, 9]
```

---

## Funções Recursivas

**10. Contagem regressiva**

**Enunciado:** Escreva uma função recursiva chamada `contar_regressivo` que recebe um número inteiro positivo e exibe os números de N até 0.

**Objetivo:** Praticar recursão e laços de repetição implícitos.

**Exemplo de saída no terminal:**

```
5
4
3
2
1
0
```
---

**11. Soma de elementos de lista**

**Enunciado:** Crie uma função recursiva chamada `somar_elementos` que recebe uma lista de números e retorna a soma de seus elementos.

**Objetivo:** Treinar recursão com listas.

**Exemplo de saída no terminal:**

```
Soma da lista [1, 2, 3, 4] é 10
```
---

**12. N-ésimo número de Fibonacci**

**Enunciado:** Implemente uma função recursiva chamada `calcular_fibonacci` que retorna o N-ésimo número da sequência de Fibonacci.

**Objetivo:** Praticar recursão e lógica matemática.

**Exemplo de saída no terminal:**

```
O 6º número de Fibonacci é 8
O 10º número de Fibonacci é 55
```

---

## Uso de Docstrings e Anotações de Tipo

**13. Converter distância**

**Enunciado:** Crie uma função chamada `converter_distancia` que converte quilômetros em milhas. Adicione anotações de tipo e uma docstring detalhada.

**Objetivo:** Praticar boas práticas de documentação e tipagem.

**Exemplo de saída no terminal:**

```
10 km equivalem a 6.21 milhas
```
---

**14. Verificar número primo**

**Enunciado:** Implemente uma função `verificar_primo` que recebe um número inteiro positivo e retorna um booleano indicando se é primo. Inclua docstring e anotações de tipo.

**Objetivo:** Praticar docstrings e lógica matemática.

**Exemplo de saída no terminal:**

```
7 é primo: True
10 é primo: False
```
---

**15. Calcular desconto**

**Enunciado:** Escreva uma função `calcular_desconto` que recebe o preço original e a porcentagem de desconto e retorna o preço final. Inclua docstring e anotações de tipo.

**Objetivo:** Aplicar docstrings, anotações de tipo e cálculos.

**Exemplo de saída no terminal:**

```
Preço original: 200, Desconto: 10% → Preço final: 180.0
```

---

## Inner Functions

**16. Mensagens curtas e longas**

**Enunciado:** Crie duas funções `curta` e `longa` que retornam mensagens curtas e longas. Crie uma terceira função `mensagem` que recebe uma das funções como argumento e a executa passando um nome.

**Objetivo:** Praticar funções como argumentos.

**Exemplo de saída no terminal:**

```
Olá, João! (mensagem curta)
Olá, João! Hoje foi um dia incrível e cheio de aprendizados! (mensagem longa)
```
---

**17. Funções internas**

**Enunciado:** Crie uma função `pai` que contenha duas funções internas. A função externa deve imprimir uma mensagem e chamar as internas, que também imprimem mensagens ao serem chamadas.

**Objetivo:** Treinar escopo e funções internas.

**Exemplo de saída no terminal:**

```
Mensagem da função pai
Mensagem da função filha 1
Mensagem da função filha 2
```
---

**18. Função que retorna função**

**Enunciado:** Crie uma função `calcular` que receba um operador (`"+"` ou `"-"`) e retorne outra função que realiza a operação correspondente entre dois números. Caso o operador seja inválido, retorne uma função que informe isso.

**Objetivo:** Praticar funções de ordem superior e retorno de funções.

**Exemplo de saída no terminal:**

```
Soma: 10
Subtração: 5
Operador inválido
```

---

## Funções Built-in Simples

**19. Contar elementos de uma lista**

**Enunciado:** Crie uma lista de frutas e use uma função built-in para exibir quantos elementos ela possui.

**Objetivo:** Praticar o uso da função `len()`.

**Exemplo de saída no terminal:**

```
A lista possui 5 elementos
```
---

**20. Soma de elementos**

**Enunciado:** Crie uma lista de números e use uma função built-in para calcular a soma de todos os elementos.

**Objetivo:** Praticar o uso da função `sum()`.

**Exemplo de saída no terminal:**

```
A soma dos números é 45
```
---

**21. Encontrar maior e menor número**

**Enunciado:** Crie uma lista de números e use funções built-in para encontrar o maior e o menor valor.

**Objetivo:** Praticar `max()` e `min()`.

**Exemplo de saída no terminal:**

```
Maior número: 20
Menor número: 3
```

---

## Funções de Ordem Superior

**22. Dobrar valores com `map()`**

**Enunciado:** Crie uma lista de números e use `map()` com uma função lambda para dobrar cada valor.

**Objetivo:** Praticar funções de ordem superior.

**Exemplo de saída no terminal:**

```
Lista original: [1, 2, 3]
Lista dobrada: [2, 4, 6]
```
---

**23. Filtrar números pares com `filter()`**

**Enunciado:** Use `filter()` e uma função lambda para extrair apenas os números pares de uma lista.

**Objetivo:** Praticar `filter()` e lógica condicional.

**Exemplo de saída no terminal:**

```
Números pares: [2, 4, 6]
```
---

**24. Verificação com `any()` e `all()`**

**Enunciado:** Dada uma lista de booleanos `[True, False, True]`, use `any()` e `all()` para verificar condições.

**Objetivo:** Aprender a verificar múltiplas condições de forma rápida.

**Exemplo de saída no terminal:**

```
Existe algum True? True
Todos são True? False
```

---

## Funções de Iteráveis

**25. Enumerar elementos com `enumerate()`**

**Enunciado:** Crie uma lista de nomes e use `enumerate()` para exibir cada elemento junto com seu índice.

**Objetivo:** Praticar iteração com índice.

**Exemplo de saída no terminal:**

```
0 - Alice
1 - Bruno
2 - Carla
```
---

**26. Inverter elementos com `reversed()`**

**Enunciado:** Crie uma lista de números e exiba a lista invertida usando `reversed()`.

**Objetivo:** Praticar funções para manipulação de ordem em iteráveis.

**Exemplo de saída no terminal:**

```
Lista invertida: [5, 4, 3, 2, 1]
```
---

**27. Agrupar listas com `zip()`**

**Enunciado:** Crie duas listas, uma com nomes e outra com idades. Use `zip()` para exibir nome e idade juntos.

**Objetivo:** Praticar a combinação de iteráveis.

**Exemplo de saída no terminal:**

```
Alice - 25
Bruno - 30
Carla - 28
```

---

## Funções de Conversão

**28. Converter tipos com `int()`, `float()` e `str()`**

**Enunciado:** Peça para o usuário digitar um número, converta-o em inteiro, depois em float e por fim em string, exibindo cada conversão.

**Objetivo:** Praticar conversão de tipos.

**Exemplo de saída no terminal:**

```
Número digitado: 10
Como inteiro: 10
Como float: 10.0
Como string: '10'
```
---

**29. Converter valores booleanos com `bool()`**

**Enunciado:** Dada uma lista `[0, 1, "", "Texto", [], [1]]`, use `bool()` para verificar o valor booleano de cada elemento.

**Objetivo:** Praticar conversão explícita em booleanos.

**Exemplo de saída no terminal:**

```
0 → False
1 → True
"" → False
"Texto" → True
[] → False
[1] → True
```

---

## Funções Especiais de Strings e Listas

**30. Separar e juntar strings com `split()` e `join()`**

**Enunciado:** Dada a frase `"Python é incrível"`, use `split()` para separar em palavras e `join()` para juntar com hífen `-`.

**Objetivo:** Praticar manipulação de strings.

**Exemplo de saída no terminal:**

```
Lista de palavras: ['Python', 'é', 'incrível']
Frase unida: Python-é-incrível
```
---

**31. Ordenar listas com `sorted()`**

**Enunciado:** Crie uma lista de números e exiba uma versão ordenada usando `sorted()`, sem alterar a lista original.

**Objetivo:** Praticar ordenação sem modificar a lista original.

**Exemplo de saída no terminal:**

```
Lista original: [5, 2, 9, 1]
Lista ordenada: [1, 2, 5, 9]
```
---

**32. Contar ocorrências com `count()`**

**Enunciado:** Crie uma lista de frutas com repetições e use `count()` para saber quantas vezes `"maçã"` aparece.

**Objetivo:** Praticar contagem de elementos em listas.

**Exemplo de saída no terminal:**

```
Maçã aparece 3 vezes na lista
```

---