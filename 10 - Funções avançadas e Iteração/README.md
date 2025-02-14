# Funções avançadas e Iteração

## 1. Decorador simples 

**Enunciado:**  
Crie um decorador que modifique o comportamento de uma função, adicionando a execução de um código antes e depois da função original. Em seguida, aplique esse decorador a uma função simples e observe o resultado ao chamá-la.  

**Objetivo:**  
Compreender o funcionamento de decoradores, que permitem modificar funções sem alterar seu código diretamente.

## 2. Decorador com Argumentos  

**Enunciado:**  
Crie um decorador que exiba mensagens antes e depois da execução de uma função. A função decorada deve receber um argumento e utilizá-lo na sua execução. Teste o decorador aplicando-o a uma função que exibe um nome formatado.  

**Objetivo:**  
Entender como decoradores podem manipular funções que recebem argumentos, utilizando `*args` e `**kwargs` para maior flexibilidade.

## 3. Decorador com Retorno  

**Enunciado:**  
Crie um decorador que modifique uma função para exibir uma mensagem antes e depois da execução, garantindo que o valor retornado pela função decorada seja preservado e exibido. Teste aplicando o decorador a uma função que retorna uma saudação personalizada.  

**Objetivo:**  
Compreender como os decoradores podem modificar funções sem alterar seu retorno, garantindo a correta manipulação dos valores devolvidos pela função decorada.  


## 4. Decorador com Parâmetro  

**Enunciado:**  
Implemente um decorador que receba um argumento numérico e utilize esse valor para repetir a execução da função decorada. A função decorada deve exibir uma saudação, e o decorador deve garantir que ela seja chamada múltiplas vezes conforme o valor passado.  

**Objetivo:**  
Aprender a criar decoradores que aceitam argumentos, entendendo a estrutura de funções aninhadas para modificar dinamicamente o comportamento de outras funções.

## 5. Criando um Iterador Personalizado  

**Enunciado:**  
Implemente uma classe que funcione como um iterador personalizado. Essa classe deve receber uma lista de números e, ao ser percorrida em um loop, retornar cada número multiplicado por 2. Se os elementos da lista acabarem, a iteração deve ser finalizada corretamente.  

**Objetivo:**  
Compreender a implementação de iteradores personalizados em Python utilizando os métodos `__iter__()` e `__next__()`, além do tratamento de exceções com `StopIteration`.

## 6. Criando um Gerador Personalizado  

**Enunciado:**  
Implemente uma função geradora que produza uma sequência de números de 0 a 9, retornando cada número multiplicado por 2. Utilize um loop para percorrer e exibir os valores gerados.  

**Objetivo:**  
Compreender o funcionamento de geradores em Python, utilizando a palavra-chave `yield` para produzir valores sob demanda de forma eficiente.