# A Sintaxe Básica

## 1. Hello, Python

- Escreva um programa que exiba a mensagem:  

  ```text
  Olá, Mundo!
  Bem-vindo ao universo Python!
  ```

## 2. Soma de Dois Números

- Solicite ao usuário dois números e exiba a soma.

  **Entrada esperada:**  

  ```powershell
  Digite o primeiro número: 10
  Digite o segundo número: 5
  ```  

  **Saída esperada:**  

  ```powershell
  A soma é 15
  ```

## 3. Conversor de Temperatura

- Converta uma temperatura de Celsius para Fahrenheit.
A fórmula é: `F = (C × 9/5) + 32`

  **Entrada:**

  ```powershell
  Digite a temperatura em Celsius: 25
  ```  

  **Saída:**  

  ```powershell
  A temperatura em Fahrenheit é 77.0
  ```

## 4. Par ou Ímpar

- Peça um número ao usuário e diga se ele é par ou ímpar.  

## 5. Calculadora de IMC

- Peça o peso e a altura do usuário e calcule seu IMC.
A fórmula é: `IMC = Peso/altura²`  
- Informe se ele está abaixo do peso, no peso ideal ou acima do peso.  

## 6. Calcule a Área do Círculo

- Peça o raio de um círculo e calcule sua área.
Fórmula: `A = π.raio²`

## 7. Conversor de Minutos para Horas

- Peça ao usuário uma quantidade de minutos e converta para horas e minutos.  
  **Entrada:**  

  ```powershell
  Digite o tempo em minutos: 125
  ```  

  **Saída:**  

  ```powershell
  125 minutos equivalem a 02h05min
  ```

## 8. Calculadora de Descontos

- Peça o preço original de um produto e a porcentagem de desconto. Calcule e exiba o valor final.  

## 9. Média de Três Notas

- Solicite três notas de um aluno, calcule a média e informe se ele foi aprovado (média >= 7).  

## 10. Operações Matemáticas

- Crie um programa que peça dois números ao usuário e mostre o resultado das quatro operações: soma, subtração, multiplicação e divisão.  

## 11. Número Maior

- Peça três números ao usuário e diga qual é o maior.  

## 12. Tabuada

**Enunciado:**  
Peça ao usuário um número inteiro `X` e exiba a tabuada desse número de 1 a 10 utilizando um laço `for`.  

**Exemplo de saída:**  

```powershell
Digite um número: 7
Tabuada de 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```  

## 13. Soma de Números  

**Enunciado:**  
Peça ao usuário um número inteiro positivo `N` e calcule a soma de todos os números inteiros de 1 a `N` utilizando um laço de repetição `for`.  

**Exemplo de saída:**  

```powershell
Digite um número inteiro positivo: 5
A soma de 1 a 5 é: 15
```

## 14. Validação de Senha  

**Enunciado:**  
Peça ao usuário que insira uma senha. Utilize um laço `while` para repetir o pedido até que ele insira a senha correta (por exemplo, "12345").  

**Exemplo de saída:**  

```powershell
Digite a senha: 54321
Senha incorreta. Tente novamente.
Digite a senha: 12345
Senha correta. Bem-vindo!
```

## 15. Contagem regressiva com condição (com `while`)**  

**Objetivo:** Praticar o uso do laço `while` e controle de fluxo com decremento.

**Instruções:**  
Escreva um programa que faça uma contagem regressiva a partir de um número fornecido pelo usuário. A contagem deve seguir de acorco com a interação do usuario e parar se atingir zero ou se o usuário interromper o processo digitando um comando específico, como `"parar"`.

**Requisitos:**  

1. Solicite ao usuário um número inteiro positivo para iniciar a contagem regressiva.
2. Utilize um laço `while` para decrementar o número e exibir a contagem a cada iteração.  
3. Durante a contagem, permita que o usuário digite `"parar"` para interromper.  

**Exemplo de saída esperada:**  

```powershell
Digite um número para começar a contagem regressiva: 5  
5 
Digite "parar" para interromper ou pressione Enter para continuar:  
4  
Digite "parar" para interromper ou pressione Enter para continuar: parar  
Contagem interrompida!  
```

## 16. Reversor de Nomes

- Solicite o nome do usuário e exiba-o ao contrário.  
  **Entrada:**  

  ```powershell
  Digite seu nome: Ricardo
  ```  

  **Saída:**

  ```powershell
  Seu nome ao contrário é: odraciR
  ```

## 17. Contador de Palavras

- Peça uma frase ao usuário e mostre quantas palavras ela possui.  

Aqui estão três exercícios sobre manipulação de strings:  

## 18. Palíndromo

**Objetivo:** Verificar se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente).  

**Instruções:**  
Escreva um programa que receba uma palavra ou frase do usuário e verifique se ela é um palíndromo. Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

**Requisitos:**  

1. Use o metodo `replace()` para remover os espaços.  
2. Converta todos os caracteres para minúsculas para garantir a consistência da comparação.  
3. Informe ao usuário se a entrada é ou não um palíndromo.

**Exemplo de saída esperada:**  

```powershell
Digite uma palavra ou frase: Apos a sopa  
É um palíndromo!  
```

```powershell
Digite uma palavra ou frase: Python  
Não é um palíndromo.  
```

## 19. Contador de vogais e consoantes  

**Objetivo:** Contar o número de vogais e consoantes em uma palavra ou frase fornecida pelo usuário.  

**Instruções:**  
Escreva um programa que receba uma palavra ou frase e conte quantas vogais e consoantes existem nela. Ignore números, espaços e caracteres especiais.

**Requisitos:**  

1. Converta a entrada para minúsculas para facilitar a contagem.  
2. Use um laço para verificar cada caractere da string.  
3. Informe ao usuário o total de vogais e consoantes encontradas.  

**Exemplo de saída esperada:**  

```powershell
Digite uma palavra ou frase: OpenAI é incrível!  
Vogais: 7  
Consoantes: 6  
```

## 20. Substituir palavras em uma frase

**Objetivo:** Praticar substituição de substrings em strings.  

**Instruções:**  
Escreva um programa que solicite ao usuário uma frase, uma palavra para substituir e uma palavra nova para colocar no lugar. O programa deve exibir a frase resultante com as alterações.  

**Requisitos:**  

1. Use o método `replace()` para realizar a substituição.  
2. O programa deve ser sensível ao uso de maiúsculas e minúsculas na palavra a ser substituída.  
3. Informe ao usuário a frase final com a substituição.  

**Exemplo de saída esperada:**  

```powershell
Digite uma frase: Eu gosto de Python.  
Digite a palavra que deseja substituir: Python  
Digite a nova palavra: programação  
Frase atualizada: Eu gosto de programação.  
```
