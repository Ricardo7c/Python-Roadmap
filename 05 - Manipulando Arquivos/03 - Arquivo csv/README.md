# 📌 Exercícios – Manipulação de Arquivos CSV (`csv.reader`, `csv.writer`)

---

### **1. Criar CSV simples**

**Enunciado:** Crie um arquivo `alunos.csv` com cabeçalho (`nome,idade,curso`) e três registros de alunos.

**Objetivo:** Aprender a criar e gravar dados tabulares em CSV.

**Requisitos de Conhecimento:** `import csv`, `with open()`, `csv.writer()`, `writerow()`.

**Exemplo de Saída no Terminal:**

```
Arquivo 'alunos.csv' criado com 3 registros.
```

---

### **2. Ler CSV linha a linha**

**Enunciado:** Abra `alunos.csv` e exiba cada linha no terminal.
**Objetivo:** Entender como `csv.reader()` retorna listas para cada linha.

**Requisitos de Conhecimento:** `csv.reader()`, `for row in reader`.

**Exemplo de Saída no Terminal:**

```
['nome', 'idade', 'curso']
['Ana', '21', 'Engenharia']
['Carlos', '19', 'Medicina']
['João', '22', 'Direito']
```

---

### **3. Exibir CSV formatado**

**Enunciado:** Leia `alunos.csv` e exiba os dados formatados, ignorando o cabeçalho.
**Objetivo:** Praticar como pular o cabeçalho e formatar saída.

**Requisitos de Conhecimento:** `next(reader)`, f-strings.

**Exemplo de Saída no Terminal:**

```
Aluno: Ana | Idade: 21 | Curso: Engenharia
Aluno: Carlos | Idade: 19 | Curso: Medicina
Aluno: João | Idade: 22 | Curso: Direito
```

---

### **4. Adicionar nova linha**

**Enunciado:** Adicione um novo aluno (`Marina,20,Arquitetura`) ao arquivo `alunos.csv`.

**Objetivo:** Aprender a abrir em modo append e usar `writerow()`.

**Requisitos de Conhecimento:** `with open(..., 'a')`, `writerow()`.
**Exemplo de Saída no Terminal:**

```
Novo aluno adicionado ao arquivo.
```

---

### **5. Criar CSV de produtos**

**Enunciado:** Crie um arquivo `produtos.csv` com cabeçalho (`produto,preco,quantidade`) e pelo menos 3 registros.

**Objetivo:** Reforçar a criação de tabelas CSV.

**Requisitos de Conhecimento:** `csv.writer()`, listas.
**Exemplo de Saída no Terminal:**

```
Arquivo 'produtos.csv' criado com 3 produtos.
```

---

### **6. Calcular total de estoque**

**Enunciado:** Leia `produtos.csv` e calcule o valor total do estoque (preço × quantidade para cada produto).

**Objetivo:** Praticar leitura de CSV e conversão de strings para `int`/`float`.

**Requisitos de Conhecimento:** `csv.reader()`, `float()`, `int()`.
**Exemplo de Saída no Terminal:**

```
Valor total do estoque: 872.50
```

---

### **7. Filtrar produtos por preço**

**Enunciado:** Leia `produtos.csv` e exiba apenas os produtos com preço acima de R$ 2.
**Objetivo:** Trabalhar filtragem de dados em CSV.

**Requisitos de Conhecimento:** `csv.reader()`, condicionais.

**Exemplo de Saída no Terminal:**

```
Produto: Maçã | Preço: R$ 2.50 | Quantidade: 100
Produto: Laranja | Preço: R$ 3.00 | Quantidade: 120
```

---

### **8. Ler CSV em lista de dicionários**

**Enunciado:** Reescreva a leitura de `produtos.csv`, mas salve cada linha como um dicionário com as chaves sendo os nomes do cabeçalho.

**Objetivo:** Praticar a construção de estruturas de dados mais úteis a partir de CSV.

**Requisitos de Conhecimento:** `next(reader)` para cabeçalho, `zip()`, listas, dicionários.

**Exemplo de Saída no Terminal:**

```
[{'produto': 'Notebook', 'preco': '3500', 'quantidade': '5'}, ...]
```

---

### **9. Criar relatório CSV**

**Enunciado:** Leia `produtos.csv`, calcule o valor total de cada produto (preço × quantidade) e grave em `relatorio.csv` com cabeçalho (`produto,valor_total`).

**Objetivo:** Praticar leitura, processamento e gravação em outro CSV.

**Requisitos de Conhecimento:** `csv.reader()`, `csv.writer()`, cálculos.
**Exemplo de Saída no Terminal:**

```
Relatório salvo em 'relatorio.csv'.
```

---

### **10. Converter CSV em lista formatada**

**Enunciado:** Leia `alunos.csv` e salve todos os nomes em uma lista Python chamada `nomes`.

**Objetivo:** Extrair informações específicas de um CSV para listas Python.

**Requisitos de Conhecimento:** `csv.reader()`, listas.
**Exemplo de Saída no Terminal:**

```
['Ana', 'Carlos', 'João', 'Marina']
```

---

Quer que eu já prepare a última parte (**arquivos binários: `'rb'`, `'wb'`, `pickle`**) ou prefere resolver os de **CSV** primeiro e só depois avançar?
