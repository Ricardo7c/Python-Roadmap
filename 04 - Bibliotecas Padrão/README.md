# Bibliotecas padrão

## 1. Jogo de Adivinhação (Usando `random`)

**Objetivo**: Criar um jogo onde o jogador deve adivinhar um número gerado aleatoriamente.

**Instruções**:  

- Use a biblioteca `random` para gerar um número inteiro entre 1 e 10.
- Peça ao jogador para adivinhar o número.
- Informe se o palpite é maior ou menor que o número sorteado.
- O jogo continua até o jogador acertar o número.
- Exiba a quantidade de tentativas no final.

---

## 2. Calculadora de Diferença de Datas (Usando `datetime`)

**Objetivo**: Criar um programa que calcula a diferença entre duas datas fornecidas pelo usuário.

**Instruções**:

1. Use a biblioteca `datetime` para trabalhar com datas.
2. Solicite ao usuário duas datas no formato `DD/MM/AAAA`.
3. Calcule a diferença em dias entre as duas datas.
4. Exiba a diferença.

---

## 3. Explorando a Biblioteca `math`

**Objetivo**: Neste exercício, você irá explorar algumas funções úteis da biblioteca `math` para realizar operações matemáticas simples como calcular raízes quadradas, potências, o valor de pi e funções trigonométricas.

**Instruções**:

- **Calcule a raiz quadrada** de um número. Por exemplo, calcule a raiz quadrada de 16.
- **Exiba o valor de pi** utilizando a constante `math.pi`.
- **Calcule a potência** de um número. Por exemplo, calcule `2` elevado a `3` utilizando `math.pow()`.
- **Calcule o cosseno** de um ângulo, utilizando a função `math.cos()`. Antes de calcular, converta o valor do ângulo de graus para radianos com `math.radians()`. Exemplo: calcule o cosseno de 45 graus.

---

## 4. Validação de E-mails

**Enunciado**:  
Implemente uma função chamada `validar_email` que recebe uma string representando um e-mail e verifica se ele é válido usando expressões regulares.  

Um e-mail válido deve obedecer às seguintes regras:  

- Deve conter um nome de usuário (letras, números, pontos ou sublinhados).
- Deve ter o símbolo `@`.  
- Deve conter um domínio (letras ou números).  
- Deve terminar com uma extensão de domínio (como `.com`, `.org`, `.br`).  

**Requisitos**:  

- Se o e-mail for válido, a função deve retornar `True`.
- Caso contrário, deve retornar `False`.  

---

## 05. Extração de Números de uma String

**Enunciado**:  
Crie uma função chamada `extrair_numeros` que recebe uma string como entrada e retorna uma lista com todos os números encontrados na string usando expressões regulares.  

**Requisitos**:  

- Use a função `re.findall` para capturar os números.  
- Os números podem ser inteiros ou decimais.  
- Caso nenhum número seja encontrado, a função deve retornar uma lista vazia.  

---
