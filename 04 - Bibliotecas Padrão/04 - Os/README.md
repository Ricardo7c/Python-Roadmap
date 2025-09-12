# 📌 Exercícios – Biblioteca `os`

---

### **1. Diretório Atual**

**Enunciado:** Crie um programa que exiba o diretório de trabalho atual usando `os.getcwd()`.
**Objetivo:** Aprender a identificar onde o programa está sendo executado.
**Requisitos de Conhecimento:** `import os`, `os.getcwd()`.
**Exemplo de Saída no Terminal:**

```
Diretório atual: C:\Users\Ricardo\Projetos
```

---

### **2. Listando Arquivos**

**Enunciado:** Liste todos os arquivos e pastas presentes no diretório atual usando `os.listdir()`.
**Objetivo:** Praticar listagem de conteúdo de diretórios.
**Requisitos de Conhecimento:** `os.listdir()`.
**Exemplo de Saída no Terminal:**

```
Conteúdo do diretório:
['main.py', 'dados.txt', 'imagens', 'exercicios']
```

---

### **3. Criando uma Pasta**

**Enunciado:** Solicite ao usuário o nome de uma nova pasta e crie-a no diretório atual usando `os.mkdir()`.
**Objetivo:** Praticar criação de diretórios.
**Requisitos de Conhecimento:** `os.mkdir()`.
**Exemplo de Saída no Terminal:**

```
Digite o nome da pasta: teste
Pasta 'teste' criada com sucesso!
```

---

### **4. Removendo uma Pasta**

**Enunciado:** Peça ao usuário o nome de uma pasta vazia e remova-a usando `os.rmdir()`.
**Objetivo:** Treinar remoção de diretórios.
**Requisitos de Conhecimento:** `os.rmdir()`.
**Exemplo de Saída no Terminal:**

```
Digite o nome da pasta para remover: teste
Pasta 'teste' removida com sucesso!
```

---

### **5. Renomeando Arquivos ou Pastas**

**Enunciado:** Solicite ao usuário o nome de um arquivo/pasta existente e um novo nome, e renomeie usando `os.rename()`.
**Objetivo:** Aprender a renomear arquivos e pastas.
**Requisitos de Conhecimento:** `os.rename()`.
**Exemplo de Saída no Terminal:**

```
Digite o nome do arquivo/pasta: dados.txt
Digite o novo nome: dados_antigos.txt
'dados.txt' foi renomeado para 'dados_antigos.txt'
```

---

### **6. Removendo Arquivos**

**Enunciado:** Peça ao usuário o nome de um arquivo e remova-o usando `os.remove()`.
**Objetivo:** Praticar exclusão de arquivos.
**Requisitos de Conhecimento:** `os.remove()`.
**Exemplo de Saída no Terminal:**

```
Digite o nome do arquivo para remover: dados_antigos.txt
Arquivo 'dados_antigos.txt' removido com sucesso!
```

---

### **7. Verificando Existência**

**Enunciado:** Solicite ao usuário um nome de arquivo ou pasta e verifique se ele existe usando `os.path.exists()`.
**Objetivo:** Praticar verificação de caminhos.
**Requisitos de Conhecimento:** `os.path.exists()`.
**Exemplo de Saída no Terminal:**

```
Digite o caminho: exercicios
O caminho existe!
```

---

### **8. Juntando Caminhos**

**Enunciado:** Peça ao usuário o nome de uma pasta e de um arquivo, e crie o caminho completo usando `os.path.join()`.
**Objetivo:** Aprender a montar caminhos de forma segura.
**Requisitos de Conhecimento:** `os.path.join()`.
**Exemplo de Saída no Terminal:**

```
Digite a pasta: documentos
Digite o arquivo: resumo.txt
Caminho completo: documentos/resumo.txt
```

---