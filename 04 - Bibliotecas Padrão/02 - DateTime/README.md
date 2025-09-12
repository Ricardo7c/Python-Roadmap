# 📌 Exercícios – Biblioteca `datetime`

---

### **1. Data e Hora Atuais**

**Enunciado:** Crie um programa que exiba a data e a hora atuais usando `datetime.now()`.

**Objetivo:** Praticar a obtenção de data e hora do sistema.

**Requisitos de Conhecimento:** `import datetime`, `datetime.now()`.

**Exemplo de Saída no Terminal:**

```
Data e hora atuais: 2025-09-12 09:45:32.412583
```

---

### **2. Data Atual Simples**

**Enunciado:** Exiba apenas a data atual (sem hora) usando `datetime.today()`.

**Objetivo:** Praticar a diferença entre `now()` e `today()`.

**Requisitos de Conhecimento:** `datetime.today()`.

**Exemplo de Saída no Terminal:**

```
Data de hoje: 2025-09-12
```

---

### **3. Formatando Datas**

**Enunciado:** Peça ao usuário que digite o seu nome e exiba uma mensagem de boas-vindas mostrando a data atual formatada no estilo `dd/mm/aaaa`. Use `strftime()`.

**Objetivo:** Praticar formatação de datas.

**Requisitos de Conhecimento:** `strftime()`.

**Exemplo de Saída no Terminal:**

```
Digite seu nome: Ricardo
Bem-vindo, Ricardo! Hoje é 12/09/2025
```

---

### **4. Formatando Horários**

**Enunciado:** Exiba a hora atual no formato `HH:MM:SS` usando `strftime()`.

**Objetivo:** Treinar formatação de hora.

**Requisitos de Conhecimento:** `strftime()`.

**Exemplo de Saída no Terminal:**

```
Hora atual: 09:47:05
```

---

### **5. Convertendo String para Data**

**Enunciado:** Peça ao usuário que digite uma data no formato `dd/mm/aaaa` e converta essa string em um objeto `datetime` usando `strptime()`.

**Objetivo:** Praticar conversão de texto para data.

**Requisitos de Conhecimento:** `strptime()`.

**Exemplo de Saída no Terminal:**

```
Digite uma data (dd/mm/aaaa): 25/12/2025
Data convertida: 2025-12-25 00:00:00
```

---

### **6. Diferença de Dias**

**Enunciado:** Solicite que o usuário digite a sua data de nascimento e calcule quantos dias se passaram desde então até hoje. Use `strptime()` e `timedelta`.

**Objetivo:** Trabalhar com diferença de datas.

**Requisitos de Conhecimento:** `strptime()`, `timedelta`.

**Exemplo de Saída no Terminal:**

```
Digite sua data de nascimento (dd/mm/aaaa): 10/05/2000
Você já viveu 9265 dias!
```

---

### **7. Contagem Regressiva**

**Enunciado:** Peça ao usuário uma data futura e calcule quantos dias faltam para ela chegar.

**Objetivo:** Praticar cálculo com datas futuras.

**Requisitos de Conhecimento:** `strptime()`, `timedelta`.

**Exemplo de Saída no Terminal:**

```
Digite uma data futura (dd/mm/aaaa): 01/01/2026
Faltam 111 dias para essa data!
```

---

### **8. Adicionando Dias**

**Enunciado:** Mostre a data atual e depois exiba qual será a data daqui a 30 dias, usando `timedelta`.

**Objetivo:** Praticar soma de datas com `timedelta`.

**Requisitos de Conhecimento:** `timedelta(days=N)`.

**Exemplo de Saída no Terminal:**

```
Hoje: 12/09/2025
Daqui a 30 dias: 12/10/2025
```

---

### **9. Subtraindo Dias**

**Enunciado:** Mostre qual era a data exata há 100 dias atrás a partir da data atual.

**Objetivo:** Usar `timedelta` para subtração de datas.

**Requisitos de Conhecimento:** `timedelta(days=N)`.

**Exemplo de Saída no Terminal:**

```
A data de 100 dias atrás era: 04/06/2025
```

---

### **10. Dias até o Aniversário**

**Enunciado:** Peça ao usuário a data do seu próximo aniversário e calcule quantos dias faltam para ele.

**Objetivo:** Exercício de aplicação prática com `datetime` e `timedelta`.

**Requisitos de Conhecimento:** `strptime()`, `today()`, `timedelta`.

**Exemplo de Saída no Terminal:**

```
Digite sua data de aniversário (dd/mm/aaaa): 10/05/2026
Faltam 241 dias para o seu aniversário!
```

---
