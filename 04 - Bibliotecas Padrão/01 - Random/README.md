# 📌 Exercícios – Biblioteca `random`

### **1. Número Aleatório Simples**

**Enunciado:** Crie um programa que exiba um número aleatório entre 0.0 e 1.0 usando `random()`.

**Objetivo:** Praticar o uso básico de geração de números aleatórios.

**Requisitos de Conhecimento:** `import`, função `random.random()`, `print()`.

**Exemplo de Saída no Terminal:**

```
Número gerado: 0.736482
```

---

### **2. Número Inteiro Aleatório**

**Enunciado:** Peça ao usuário para digitar dois números inteiros (início e fim) e exiba um número aleatório dentro desse intervalo usando `randint()`.

**Objetivo:** Praticar o uso de `randint()`.

**Requisitos de Conhecimento:** `input()`, conversão `int()`, `random.randint()`.

**Exemplo de Saída no Terminal:**

```
Digite o início: 10
Digite o fim: 20
Número sorteado: 14
```

---

### **3. Número Real Aleatório**

**Enunciado:** Solicite ao usuário dois valores (mínimo e máximo) e exiba um número aleatório float nesse intervalo usando `uniform()`.

**Objetivo:** Praticar o uso de `uniform()`.

**Requisitos de Conhecimento:** `input()`, `float()`, `random.uniform()`, `f-string`.

**Exemplo de Saída no Terminal:**

```
Digite o valor mínimo: 1.5
Digite o valor máximo: 5.5
Número sorteado: 3.7
```

---

### **4. Escolha Aleatória de Lista**

**Enunciado:** Crie uma lista com 5 nomes e exiba um nome aleatório usando `choice()`.

**Objetivo:** Praticar a seleção de elementos aleatórios em listas.

**Requisitos de Conhecimento:** listas, `random.choice()`.

**Exemplo de Saída no Terminal:**

```
Nome sorteado: Mariana
```

---

### **5. Sorteio de Itens com Repetição**

**Enunciado:** Crie uma lista com 6 números. Faça um sorteio de 3 números com repetição usando `choices()`.

**Objetivo:** Praticar `random.choices()`.

**Requisitos de Conhecimento:** listas, `random.choices()`.

**Exemplo de Saída no Terminal:**

```
Números sorteados: [4, 2, 4]
```

---

### **6. Sorteio de Itens sem Repetição**

**Enunciado:** Crie uma lista de 10 números e sorteie 4 elementos **sem repetição** usando `sample()`.

**Objetivo:** Diferenciar `choices()` de `sample()`.

**Requisitos de Conhecimento:** listas, `random.sample()`.

**Exemplo de Saída no Terminal:**

```
Números sorteados: [8, 2, 10, 6]
```

---

### **7. Embaralhando uma Lista**

**Enunciado:** Crie uma lista de 10 cartas (pode ser números de 1 a 10). Embaralhe a lista usando `shuffle()` e mostre a nova ordem.

**Objetivo:** Praticar embaralhamento de listas.

**Requisitos de Conhecimento:** listas, `random.shuffle()`.

**Exemplo de Saída no Terminal:**

```
Ordem original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Ordem embaralhada: [7, 2, 10, 4, 1, 6, 8, 5, 9, 3]
```

---

### **8. Simulando um Dado**

**Enunciado:** Simule o lançamento de um dado de 6 lados, exibindo o resultado entre 1 e 6.

**Objetivo:** Praticar `randint()` em uma simulação.

**Requisitos de Conhecimento:** `random.randint()`.

**Exemplo de Saída no Terminal:**

```
Você rolou o dado e saiu: 5
```

---

### **9. Loteria Simples**

**Enunciado:** Crie um programa que sorteie **6 números únicos** entre 1 e 60 (como na Mega-Sena).

**Objetivo:** Praticar `sample()` em um caso real.

**Requisitos de Conhecimento:** listas, `range()`, `random.sample()`.

**Exemplo de Saída no Terminal:**

```
Números sorteados: [3, 17, 22, 45, 51, 59]
```

---

### **10. Distribuição Gaussiana**

**Enunciado:** Gere 5 números aleatórios baseados na distribuição normal com média = 50 e desvio padrão = 10, usando `gauss()`.

**Objetivo:** Introduzir distribuições estatísticas na biblioteca `random`.

**Requisitos de Conhecimento:** laços, `random.gauss()`.

**Exemplo de Saída no Terminal:**

```
Valores gerados: [48.32, 56.11, 41.29, 62.87, 53.04]
```

---

