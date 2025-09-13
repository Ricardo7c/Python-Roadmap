# 📌 Exercícios – Biblioteca `re`

---

### **1. Validação com match**

**Enunciado:** Peça ao usuário que digite uma palavra. Verifique com `re.match()` se ela começa com a letra **"a"** e exiba o resultado.

**Objetivo:** Treinar o uso de `re.match()` para verificar o início de uma string.

**Requisitos de Conhecimento:** `import re`, `re.match()`.

**Exemplo de Saída no Terminal:**

```
Digite uma palavra: abacaxi
A palavra começa com "a".
```

---

### **2. Busca com search**

**Enunciado:** Solicite uma frase ao usuário e verifique com `re.search()` se a palavra **"python"** aparece em qualquer posição.

**Objetivo:** Praticar o uso de `re.search()` para encontrar padrões em uma string.

**Requisitos de Conhecimento:** `re.search()`.

**Exemplo de Saída no Terminal:**

```
Digite uma frase: Estou estudando python agora
A palavra "python" foi encontrada!
```

---

### **3. Encontrando todas as ocorrências**

**Enunciado:** Solicite uma frase ao usuário e utilize `re.findall()` para listar todos os números que aparecem na frase.

**Objetivo:** Extrair múltiplos padrões de uma string.

**Requisitos de Conhecimento:** `re.findall()`, expressões regulares.

**Exemplo de Saída no Terminal:**

```
Digite uma frase: Tenho 2 cachorros e 3 gatos
Números encontrados: ['2', '3']
```

---

### **4. Substituindo Texto**

**Enunciado:** Solicite uma frase ao usuário e substitua todas as ocorrências da palavra **"java"** por **"python"** usando `re.sub()`.

**Objetivo:** Aprender a substituir partes de uma string usando regex.

**Requisitos de Conhecimento:** `re.sub()`.

**Exemplo de Saída no Terminal:**

```
Digite uma frase: Eu gosto de java e java é legal
Frase modificada: Eu gosto de python e python é legal
```

---

### **5. Separando Texto**

**Enunciado:** Solicite uma frase ao usuário e use `re.split()` para separar a frase em partes, usando os espaços como delimitador.

**Objetivo:** Praticar divisão de strings usando regex.

**Requisitos de Conhecimento:** `re.split()`.

**Exemplo de Saída no Terminal:**

```
Digite uma frase: Eu estou aprendendo Python
Lista de palavras: ['Eu', 'estou', 'aprendendo', 'Python']
```

---

### **6. Compilando Regex**

**Enunciado:** Crie uma expressão regular compilada com `re.compile()` que reconheça endereços de e-mail simples (ex: [algo@dominio.com](mailto:algo@dominio.com)). Teste-a em uma frase digitada pelo usuário e exiba todos os e-mails encontrados.

**Objetivo:** Aprender a usar `re.compile()` para criar padrões reutilizáveis.

**Requisitos de Conhecimento:** `re.compile()`, `findall()`.

**Exemplo de Saída no Terminal:**

```
Digite uma frase: Meus emails são teste@gmail.com e exemplo@yahoo.com
E-mails encontrados: ['teste@gmail.com', 'exemplo@yahoo.com']
```

---
