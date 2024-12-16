# Numpy

## 1. Criação de Arrays (Básico)

Crie os seguintes arrays usando NumPy:  

1. Um array unidimensional contendo os números de 1 a 10.  
2. Um array bidimensional 3x3 contendo números de 1 a 9.  
3. Um array preenchido apenas com zeros e com 5 elementos.  
4. Um array preenchido apenas com o número 7 e com dimensões 4x2.  

---

## 2. Indexação e Fatiamento (Básico)  

Dado o seguinte array:

```python
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
```

1. Selecione o número 50 do array.  
2. Extraia a segunda linha inteira.  
3. Obtenha os números da primeira coluna.  
4. Substitua o número 90 por 99.  

---

## 3. Operações Matemáticas (Intermediário)

Crie dois arrays:  

- `a = np.array([1, 2, 3])`  
- `b = np.array([4, 5, 6])`  

1. Realize as seguintes operações: soma, subtração, multiplicação e divisão entre os arrays `a` e `b`.  
2. Eleve cada elemento do array `a` ao quadrado.  
3. Calcule a média, soma e o desvio padrão do array `b`.  
4. Crie um array resultante da multiplicação de `a` por 2 e `b` por 3.  

---

## 4. Manipulação de Arrays (Intermediário)  

Dado o array:

```python
arr = np.array([3, 6, 9, 12, 15, 18])
```

1. Redimensione-o para 2x3.  
2. Transponha o array.  
3. Adicione uma nova coluna ao array transposto com os valores `[1, 2]`.  

---

## 5. Gerar Arrays Aleatórios (Intermediário)  

1. Gere um array com 5 números aleatórios entre 0 e 1.  
2. Crie uma matriz 3x3 com números inteiros aleatórios entre 10 e 50.  
3. Encontre o maior e o menor valor no array gerado no item anterior.  

---

## 6. Funções Úteis no NumPy (Avançado)  

1. Crie um array com 100 valores uniformemente espaçados entre 0 e 10.  
2. Calcule o seno e o cosseno de todos os valores do array criado.  
3. Substitua todos os valores negativos no array do seno por 0.  

---

## 7. Condicionais e Filtragem (Avançado)  

Dado o array:

```python
data = np.array([15, 22, 8, 19, 31, 5, 13, 21])
```

1. Obtenha apenas os números maiores que 20.  
2. Substitua todos os números menores que 10 por 0.  
3. Conte quantos valores são divisíveis por 3.  

---

## 8. Operações com Matrizes (Avançado)  

Crie as matrizes:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
```

1. Realize a multiplicação elemento por elemento entre `A` e `B`.  
2. Realize o produto matricial entre `A` e `B`.  
3. Calcule o determinante de `A`.  
4. Encontre a inversa de `B`.  

---

## 9. Aplicação Prática (Avançado)  

1. Gere um array bidimensional 5x5 preenchido com números aleatórios entre 1 e 100.  
2. Substitua todos os números pares do array por -1.  
3. Ordene o array (linha por linha) em ordem crescente.  

---

## 10. Análise Estatística (Avançado)  

Dado o array:

```python
data = np.random.randint(1, 101, size=(10, 5))  # 10 linhas, 5 colunas
```

1. Encontre a média de cada coluna.  
2. Encontre a mediana de cada linha.  
3. Identifique a linha com o maior valor total (soma dos elementos).  

---
