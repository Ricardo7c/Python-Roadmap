# Funções

## Definição e Chamada de Funções

1. Crie uma função chamada `exibir_boas_vindas` que exibe a mensagem `"Bem-vindo ao curso de Python!"` quando chamada.  
Chame essa função no programa principal.
  
2. Implemente uma função chamada `mostrar_numero` que recebe um número inteiro como parâmetro e exibe: `"O número informado foi: {numero}"`.  
Teste a função passando diferentes valores.

3. Escreva uma função chamada `calcular_soma` que recebe dois números como parâmetros, calcula a soma deles e exibe o resultado.  
Teste a função no programa principal.

---

## Parâmetros e Retorno  

4.Implemente uma função chamada `calcular_area_retangulo` que recebe a largura e a altura de um retângulo como parâmetros e retorna sua área.
No programa principal, chame a função e exiba o resultado.
5. Escreva uma função chamada `verificar_paridade` que recebe um número inteiro e retorna a string `"Par"` se o número for par, ou `"Ímpar"` se for ímpar.  
Teste a função para diferentes valores.

6.Crie uma função chamada `calcular_potencia` que recebe dois números: base e expoente, e retorna o resultado da base elevada ao expoente.  
Teste a função chamando-a com diferentes valores.

---

## Funções Lambda  

7.Escreva uma função lambda que recebe dois números e retorna o maior deles.  
Use a função lambda para processar diferentes pares de números.

8.Crie uma lista de números e use uma função lambda com o método `map` para calcular o quadrado de cada número na lista.  
Exiba a lista original e a transformada.

9.Implemente uma função lambda que recebe um número e verifica se ele é divisível por 3.  
Use essa função com o método `filter` para filtrar os números divisíveis por 3 de uma lista.

---

## Funções Recursivas

*Obs.:Funções recursivas podem ser dificeis de entender, mas não precisa se assustar, você pode prosseguir no roadmap e depois revisar esse assunto com calma*

10.Escreva uma função recursiva chamada `contar_regressivo` que recebe um número inteiro positivo e exibe os números de N até 0.  
Teste a função com diferentes valores.

11.Crie uma função recursiva chamada `somar_elementos` que recebe uma lista de números e retorna a soma de seus elementos.  
Teste a função com listas de diferentes tamanhos.

12.Implemente uma função recursiva chamada `calcular_fibonacci` que retorna o N-ésimo número da sequência de Fibonacci.  
Teste a função para diferentes valores de N.

---

## Uso de Docstrings e Anotações de Tipo  

*Obs.: Anotações de tipo deixam seu codigo mais legivel e junto com uma boa Docstring deixa tudo mais profissional.*

13.Crie uma função chamada `converter_distancia` que converte uma distância de quilômetros para milhas.  
Adicione anotações de tipo para os parâmetros e o retorno e inclua uma docstring detalhada.

14.Implemente uma função chamada `verificar_primo` que recebe um número inteiro positivo como parâmetro e retorna um valor booleano indicando se o número é primo.  
Adicione anotações de tipo e uma docstring explicativa.

15.Escreva uma função chamada `calcular_desconto` que recebe o preço original de um produto e a porcentagem de desconto e retorna o preço final.  
Adicione anotações de tipo e uma docstring explicando como a função funciona.  

---

## Inner Functions

1. Crie duas funções `curta` que retorna uma msg curta e `longa` que retorna uma msg longa. Em seguida, crie uma terceira função `mensagem` que recebe uma dessas funções como argumento e a executa passando um nome específico. Teste chamando essa terceira função com as duas funções como argumento.

2. Crie uma função `pai` que contenha duas funções internas `filhas`. A função externa deve imprimir uma mensagem e chamar as funções internas em uma determinada ordem. As funções internas também devem imprimir mensagens ao serem chamadas.  

3. Crie uma função `calcular` que receba um operador matemático como argumento (`"+"` ou `"-"`) e retorne outra função que realize a operação correspondente entre dois números. Caso o operador seja inválido, retorne uma função que informe isso. Teste chamando a função retornada com dois números.
