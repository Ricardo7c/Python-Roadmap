# 📌 Exercícios – Arquivos Binários (`rb`, `wb`, `pickle`)

---

### **1. Escrever em arquivo binário**

**Enunciado:** Peça ao usuário uma frase e grave-a em um arquivo binário `mensagem.bin`.
**Objetivo:** Aprender a gravar dados em formato binário.
**Requisitos de Conhecimento:** `import pickle` , `with open(..., 'wb')`, `.encode()`.
**Exemplo de Saída no Terminal:**

```
Digite uma frase: Olá mundo
Frase salva em 'mensagem.bin'
```

---

### **2. Ler de arquivo binário**

**Enunciado:** Abra `mensagem.bin` e exiba o conteúdo decodificado como texto.
**Objetivo:** Aprender a ler arquivos binários e decodificar para string.
**Requisitos de Conhecimento:** `with open(..., 'rb')`, `.decode()`.
**Exemplo de Saída no Terminal:**

```
Conteúdo lido: Olá mundo
```

---

### **3. Serializar lista com `pickle`**

**Enunciado:** Crie uma lista Python com números de 1 a 5 e grave-a em `lista.pkl` usando `pickle.dump()`.
**Objetivo:** Aprender a salvar objetos Python em binário.
**Requisitos de Conhecimento:** `import pickle`, `with open(..., 'wb')`, `pickle.dump()`.
**Exemplo de Saída no Terminal:**

```
Lista salva em 'lista.pkl'
```

---

### **4. Desserializar lista com `pickle`**

**Enunciado:** Abra `lista.pkl` e recupere a lista usando `pickle.load()`. Exiba o conteúdo.
**Objetivo:** Aprender a carregar objetos Python de arquivos binários.
**Requisitos de Conhecimento:** `pickle.load()`.
**Exemplo de Saída no Terminal:**

```
Lista carregada: [1, 2, 3, 4, 5]
```

---

### **5. Serializar dicionário**

**Enunciado:** Crie um dicionário com informações de um usuário (nome, idade, email) e grave-o em `usuario.pkl`.
**Objetivo:** Praticar serialização de dicionários.
**Requisitos de Conhecimento:** `pickle.dump()`, dicionários.
**Exemplo de Saída no Terminal:**

```
Dicionário salvo em 'usuario.pkl'
```

---

### **6. Desserializar dicionário**

**Enunciado:** Abra `usuario.pkl`, carregue o dicionário e exiba o nome e o email.
**Objetivo:** Praticar leitura de dados complexos gravados com pickle.
**Requisitos de Conhecimento:** `pickle.load()`, acesso a dicionários.
**Exemplo de Saída no Terminal:**

```
Nome: Ricardo
Email: ricardo@example.com
```

---

### **7. Serializar múltiplos objetos**

**Enunciado:** Grave uma lista e um dicionário no mesmo arquivo `dados.pkl` (um após o outro).
**Objetivo:** Aprender que é possível armazenar mais de um objeto em sequência.
**Requisitos de Conhecimento:** `pickle.dump()` várias vezes.
**Exemplo de Saída no Terminal:**

```
Dois objetos salvos em 'dados.pkl'
```

---

### **8. Desserializar múltiplos objetos**

**Enunciado:** Abra `dados.pkl` e carregue os dois objetos salvos no exercício anterior. Exiba cada um.
**Objetivo:** Entender leitura sequencial de objetos com `pickle.load()`.
**Requisitos de Conhecimento:** `pickle.load()` múltiplas vezes.
**Exemplo de Saída no Terminal:**

```
Lista: [1, 2, 3, 4, 5]
Dicionário: {'nome': 'Ricardo', 'idade': 32}
```

---

### **9. Copiar arquivo binário**

**Enunciado:** Faça um programa que copie o conteúdo de `mensagem.bin` para `copia.bin`.
**Objetivo:** Praticar leitura e escrita em modo binário.
**Requisitos de Conhecimento:** `with open(..., 'rb')`, `with open(..., 'wb')`.
**Exemplo de Saída no Terminal:**

```
Arquivo 'mensagem.bin' copiado para 'copia.bin'
```

---

### **10. Salvar e carregar objeto complexo**

**Enunciado:** Crie um dicionário contendo listas e outros dicionários aninhados, salve-o em `complexo.pkl` e depois carregue para confirmar que os dados foram preservados.
**Objetivo:** Demonstrar que `pickle` suporta estruturas Python complexas.
**Requisitos de Conhecimento:** `pickle.dump()`, `pickle.load()`.
**Exemplo de Saída no Terminal:**

```
Objeto complexo salvo e carregado com sucesso.
```
