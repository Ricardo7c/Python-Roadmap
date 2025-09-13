# 📌 Exercícios – Biblioteca `sys`

---

### **1. Versão do Python**

**Enunciado:** Exiba a versão do Python instalada utilizando `sys.version`.

**Objetivo:** Conhecer como verificar a versão do Python em execução.

**Requisitos de Conhecimento:** `import sys`, `sys.version`.

**Exemplo de Saída no Terminal:**

```
Versão do Python: 3.12.5 (tags/v3.12.5:12345, Jul  2 2025, 10:00:00) [MSC v.1938 64 bit (AMD64)]
```

---

### **2. Sistema Operacional**

**Enunciado:** Utilize `sys.platform` para mostrar em qual sistema operacional o programa está sendo executado.

**Objetivo:** Aprender a identificar o SO pelo Python.

**Requisitos de Conhecimento:** `sys.platform`.

**Exemplo de Saída no Terminal:**

```
Sistema operacional: win32
```

---

### **3. Encerrando Programa**

**Enunciado:** Peça um número ao usuário. Se ele digitar `0`, encerre o programa usando `sys.exit()`.

**Objetivo:** Praticar encerramento de programas de forma controlada.

**Requisitos de Conhecimento:** `sys.exit()`, `input()`.

**Exemplo de Saída no Terminal:**

```
Digite um número: 0
Programa encerrado!
```

---

### **4. Argumentos de Linha de Comando**

**Enunciado:** Crie um programa que exiba todos os argumentos passados na execução usando `sys.argv`.

**Objetivo:** Compreender como capturar parâmetros pela linha de comando.

**Requisitos de Conhecimento:** `sys.argv`, execução via terminal.

**Exemplo de Saída no Terminal:**

```
> python script.py teste 123
Argumentos recebidos: ['script.py', 'teste', '123']
```

---

### **5. Primeiro Argumento**

**Enunciado:** Crie um programa que mostre apenas o primeiro argumento extra passado na execução (além do nome do arquivo).

**Objetivo:** Acessar elementos específicos de `sys.argv`.

**Requisitos de Conhecimento:** `sys.argv`, indexação de listas.

**Exemplo de Saída no Terminal:**

```
> python script.py Ricardo
Primeiro argumento: Ricardo
```

---

### **6. Contando Argumentos**

**Enunciado:** Faça um programa que conte e exiba a quantidade de argumentos recebidos na execução.

**Objetivo:** Reforçar manipulação de `sys.argv`.

**Requisitos de Conhecimento:** `len()`, `sys.argv`.

**Exemplo de Saída no Terminal:**

```
> python script.py a b c d
Quantidade de argumentos: 4
```

---

### **7. Caminhos do Python**

**Enunciado:** Exiba todos os diretórios presentes em `sys.path`.

**Objetivo:** Entender onde o Python procura módulos.

**Requisitos de Conhecimento:** `sys.path`, laços `for`.

**Exemplo de Saída no Terminal:**

```
Lista de caminhos de busca:
C:\Python312\Lib
C:\Python312\DLLs
C:\Users\Ricardo\projetos
```

---
