# 📌 Exercícios – Manipulação de Arquivos JSON

### **1. Criar arquivo JSON simples**

**Enunciado:** Crie um dicionário Python com informações de uma pessoa (nome, idade, cidade) e grave esse dicionário em um arquivo `pessoa.json` usando `json.dump()`.  

**Objetivo:** Aprender a salvar dados Python em formato JSON.  

**Requisitos de Conhecimento:** `import json`, `with open()`, `json.dump()`, dicionários.  

**Exemplo de Saída no Terminal:**
```
Arquivo 'pessoa.json' criado com sucesso.
```

### **2. Ler arquivo JSON simples**

**Enunciado:** Abra o arquivo `pessoa.json` criado no exercício anterior, carregue os dados com `json.load()` e exiba o nome e a cidade da pessoa.  

**Objetivo:** Aprender a carregar dados JSON em um dicionário Python.  

**Requisitos de Conhecimento:** `json.load()`, `with open()`, acesso a dicionários.  

**Exemplo de Saída no Terminal:**

```
    Nome: Ana
    Cidade: São Paulo
```

### **3. Lista de objetos JSON**

**Enunciado:** Crie uma lista de dicionários representando produtos (nome e preço) e salve em `produtos.json`.  

**Objetivo:** Gravar listas complexas em JSON.  

**Requisitos de Conhecimento:** listas, dicionários, `json.dump()`.  

**Exemplo de Saída no Terminal:**

```
Arquivo 'produtos.json' criado com 3 produtos.
```

### **4. Ler lista de objetos JSON**

**Enunciado:** Abra `produtos.json` e exiba cada produto no formato:

    Produto: <nome> | Preço: <preço>



**Objetivo:** Iterar sobre listas/dicionários carregados de um JSON.  
**Requisitos de Conhecimento:** `json.load()`, loops.  
**Exemplo de Saída no Terminal:**

```
Produto: Notebook | Preço: 3500
Produto: Mouse | Preço: 120
Produto: Teclado | Preço: 200
```

### **5. Atualizar JSON existente**

**Enunciado:** Abra `pessoa.json`, altere a idade para um novo valor e salve novamente o arquivo.  

**Objetivo:** Praticar leitura, modificação e regravação de JSON.  

**Requisitos de Conhecimento:** `json.load()`, `json.dump()`, manipulação de dicionários.  

**Exemplo de Saída no Terminal:**

```
Idade de 'Ana' atualizada para 26 anos.
```

### **6. JSON formatado (indentação)**

**Enunciado:** Refaça o exercício 3 (produtos), mas ao salvar use o parâmetro `indent=4` no `json.dump()` para deixar o arquivo mais legível.  

**Objetivo:** Aprender a usar opções de formatação do JSON.  

**Requisitos de Conhecimento:** `json.dump(indent=4)`.  

**Exemplo de Saída no Terminal:**

```
Arquivo 'produtos.json' criado no formato legível.
```

### **7. Ler chave inexistente com tratamento**

**Enunciado:** Abra `pessoa.json` e tente acessar a chave `"telefone"`. Caso não exista, exiba `"Telefone não informado"`.  

**Objetivo:** Trabalhar com dicionários e tratamento de ausência de dados.  

**Requisitos de Conhecimento:** `.get()` em dicionários, `json.load()`.  

**Exemplo de Saída no Terminal:**

```
Telefone não informado
```

### **8. Mesclar dados JSON**

**Enunciado:** Crie dois arquivos JSON (`clientes1.json` e `clientes2.json`), cada um com uma lista de clientes. Faça um programa que carregue ambos, junte as listas e grave em um novo arquivo `clientes.json`.  

**Objetivo:** Praticar leitura múltipla e mesclagem de dados JSON.  

**Requisitos de Conhecimento:** `json.load()`, listas, concatenação.  

**Exemplo de Saída no Terminal:**

```
Clientes mesclados em 'clientes.json'.
```

### **9. Filtrar dados de um JSON**

**Enunciado:** Dado um arquivo `produtos.json`, exiba apenas os produtos com preço acima de 500.  

**Objetivo:** Praticar filtragem de dados carregados de JSON.  

**Requisitos de Conhecimento:** `json.load()`, laços, condicionais.  

**Exemplo de Saída no Terminal:**

```
Produto: Notebook | Preço: 3500
```

### **10. Converter JSON para string e exibir**

**Enunciado:** Abra `pessoa.json`, carregue o conteúdo e exiba-o em formato de string JSON formatada usando `json.dumps()` com `indent=2`.  

**Objetivo:** Aprender a transformar dados Python em string JSON (sem salvar em arquivo).  

**Requisitos de Conhecimento:** `json.dumps()`, `indent`.  

**Exemplo de Saída no Terminal:**

```
{
  "nome": "Ana",
  "idade": 26,
  "cidade": "São Paulo"
}
```


