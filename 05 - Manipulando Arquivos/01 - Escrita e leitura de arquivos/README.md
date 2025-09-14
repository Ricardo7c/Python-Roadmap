# 📌 Exercícios – Manipulação de Arquivos

---

### **1. Criar e escrever em um arquivo**

**Enunciado:** Peça ao usuário uma mensagem e grave essa mensagem em um novo arquivo chamado `texto.txt` usando o modo `'w'`.

**Objetivo:** Praticar escrita básica em arquivos (criação/overwrite).

**Requisitos de Conhecimento:** `with open()`, `write()`, `input()`.

**Exemplo de Saída no Terminal:**

```
Digite a mensagem: Olá, mundo!
Mensagem salva em 'texto.txt'.
```

---

### **2. Adicionar (append)**

**Enunciado:** Abra o arquivo `texto.txt` do exercicio anterior no modo append (`'a'`), peça ao usuário uma linha de texto e acrescente essa linha ao final do arquivo (cada chamada adiciona uma nova linha).

**Objetivo:** Aprender a acrescentar conteúdo sem sobrescrever o existente.

**Requisitos de Conhecimento:** `with open()`, `write()`, `\n`.

**Exemplo de Saída no Terminal:**

```
Digite a linha para adicionar: Nova entrada do dia
Linha adicionada a 'texto.txt'.
```

---

### **3. Escrever múltiplas linhas**

**Enunciado:** Crie uma lista de strings (por exemplo: `["linha1\n", "linha2\n", "linha3\n"]`) e escreva todas usando `writelines()` em um arquivo `multilinhas.txt`.

**Objetivo:** Usar `writelines()` para gravar várias linhas de forma eficiente.

**Requisitos de Conhecimento:** `writelines()`, listas, `with open()`.

**Exemplo de Saída no Terminal:**

```
Arquivo 'multilinhas.txt' criado com 3 linhas.
```

---

### **4. Ler arquivo inteiro**

**Enunciado:** Crie um programa que abra um arquivo no modo leitura  `('r')`  e exiba todo o conteúdo usando `read()`.

**Objetivo:** Entender como ler todo o conteúdo de um arquivo.

**Requisitos de Conhecimento:** `with open()`, `read()`, `print()`.

**Exemplo de Saída no Terminal:**

```
Conteúdo do arquivo:
Olá, este é um arquivo de exemplo.
Aqui tem várias linhas.
```

---

### **5. Ler linha a linha**

**Enunciado:** Abra `texto.txt` e leia o arquivo linha a linha exibindo o número da linha antes de cada linha lida (ex: `1: primeira linha`). Use `readline()` ou iteração direta sobre o arquivo.

**Objetivo:** Aprender a iterar sobre linhas de um arquivo e controlar contadores.

**Requisitos de Conhecimento:** `with open()`, `readline()`.

**Exemplo de Saída no Terminal:**

```
1: Olá, este é um arquivo de exemplo.
2: Aqui tem várias linhas.
```

---

### **6. Releitura com `Open()` e `closed()`**

**Enunciado:** Refaça o exercício 4 (ler arquivo inteiro), mas utilizando open() e close().

**Objetivo:** Fixar o uso do context manager.

**Requisitos de Conhecimento:** `open()` , `read()`, `close()`.

**Exemplo de Saída no Terminal:**

```
Conteúdo do arquivo:
(igual ao exercício 4)
```

---

### **7. Copiar um arquivo de texto**

**Enunciado:** Faça um programa que copie o conteúdo de `origem.txt` para `copia.txt`. Use `with` para abrir ambos arquivos (um em `'r'`, outro em `'w'`).

**Objetivo:** Praticar leitura seguida de escrita em outro arquivo (IO básico).

**Requisitos de Conhecimento:** `with open()`, `read()`, `write()`.

**Exemplo de Saída no Terminal:**

```
Arquivo 'origem.txt' copiado para 'copia.txt'.
```

---

### **8. Substituir texto dentro do arquivo**

**Enunciado:** Abra um arquivo `dados.txt`, leia todo o conteúdo, substitua todas ocorrências de uma palavra (ex: `"foo"`) por outra (`"bar"`) usando `.replace()`, e reescreva o resultado no mesmo arquivo.

**Objetivo:** Aprender o padrão ler→modificar→escrever para edição de arquivos de texto.

**Requisitos de Conhecimento:** `with open()`, `read()`, `replace()`, escrita `'w'`.

**Exemplo de Saída no Terminal:**

```
Substituições efetuadas: 'foo' -> 'bar'
Arquivo atualizado com sucesso.
```

---

### **9. Contar linhas, palavras e caracteres**

**Enunciado:** Abra um arquivo de texto e calcule: número de linhas, número total de palavras e número total de caracteres. Exiba esses três valores.

**Objetivo:** Praticar processamento simples de texto após leitura.

**Requisitos de Conhecimento:** `with open()`, `read()`, `split()`, `len()`.

**Exemplo de Saída no Terminal:**

```
Linhas: 12
Palavras: 243
Caracteres: 1589
```

---
