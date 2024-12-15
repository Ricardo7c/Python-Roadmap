# Exceções e Erros

## 1. Tipos de Exceções Comuns

**Objetivo**: Identificar e lidar com exceções comuns em Python.

**Enunciado**: Crie um programa que solicite ao usuário dois números inteiros e exiba o resultado da divisão do primeiro pelo segundo. Garanta que o programa lide corretamente com os seguintes casos:  

- O usuário insira um valor que não seja um número (exemplo: uma string).  
- O usuário tente dividir por zero.  

**Requisitos**:  

- Use blocos `try` e `except` para capturar as exceções.  
- Informe ao usuário o motivo do erro de forma clara.  

## 2. Tratamento de Erros com `try`, `except` e `finally`

**Objetivo**: Utilizar o bloco `finally` para ações pós-execução.

**Enunciado**: Crie um programa que leia um nome de arquivo informado pelo usuário e tente abri-lo. Lide com os seguintes cenários:  

- O arquivo não existe.  
- O usuário não tem permissão para acessar o arquivo.  
- Sempre exiba a mensagem "Encerrando o programa" ao final, independente do sucesso ou erro na execução.  

**Requisitos**:  

- Use `try`, `except` e `finally`.  
- O programa deve ser resiliente e não interromper com erros inesperados.  

## 3. Levantando Exceções Personalizadas

**Objetivo**: Criar e lançar exceções personalizadas para cenários específicos.

**Enunciado**: Implemente uma função chamada `validar_idade` que receba uma idade como entrada e levante uma exceção personalizada chamada `IdadeInvalidaError` nos seguintes casos:  

- A idade seja menor que 18.  
- A idade seja maior que 100.  

Se a idade for válida, exiba a mensagem "Idade válida".  

**Requisitos**:  

- Crie uma classe para a exceção personalizada.  
- Use `raise` para lançar a exceção e `try`/`except` para tratá-la.  

## 4. Desafio: Combinação de Todos os Conceitos

**Objetivo**: Praticar o uso combinado de todos os conceitos estudados.

**Enunciado**:  Desenvolva um programa que simule o cadastro de usuários em um sistema. O programa deve:  

- Solicitar o nome do usuário.  
- Solicitar a idade do usuário e validar usando a função `validar_idade` do exercício anterior.  
- Gerar um erro se o nome do usuário contiver números ou caracteres especiais (exceto espaço).  
- Sempre exibir a mensagem "Processo de cadastro concluído" no final, independente de sucesso ou falha.  

**Requisitos**:  

- Use funções, exceções personalizadas e manipulação de erros com `try`, `except`, e `finally`.

---
