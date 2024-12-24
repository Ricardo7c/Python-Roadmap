# Construção de uma Calculadora em Tkinter

**Objetivo:**
Desenvolver uma interface gráfica para uma calculadora funcional utilizando a biblioteca Tkinter no Python. A calculadora deve permitir realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) e exibir os resultados no visor.

---

**Instruções:**

1. **Interface Gráfica:**
   - Crie uma janela principal para a calculadora com dimensões aproximadas de 280x370.
   - Adicione um visor para exibir os números digitados e os resultados das operações.
   - Organize os botões de números (0 a 9) e operações (+, -, *, /) em uma grade.

2. **Funcionalidades:**
   - Permitir a entrada de números e operações matemáticas básicas.
   - Realizar o cálculo ao pressionar o botão `=` e exibir o resultado no visor.
   - O botão `cls` deve limpar o visor e resetar os valores e operadores armazenados.
   - Prevenir erros ao tentar realizar operações inválidas, como divisão por zero, exibindo "Erro" no visor.

3. **Desafios Adicionais:**
   - Após um erro, desative os botões de operação até que o visor seja resetado.
   - Suporte para números decimais utilizando o botão `.`.
   - Implemente lógica para realizar cálculos encadeados (por exemplo, `2 + 3 * 4`).

4. **Requisitos Técnicos:**
   - Use variáveis globais para armazenar o estado da calculadora, incluindo o operador atual, o primeiro número e o status da operação.
   - Utilize funções separadas para:
     - Digitar números e operações no visor.
     - Realizar cálculos e exibir os resultados.
     - Resetar a calculadora.
     - Desativar ou ativar botões com base no estado da calculadora.

5. **Saída Esperada:**
   - Uma interface gráfica interativa que permite realizar cálculos básicos com funcionalidade robusta contra erros.
   - O visor deve exibir o resultado correto ou "Erro" em caso de operações inválidas.
   - Quando um erro acontecer os botões de operação devem ser desativados até que o usuario entre com um valor valido

---

**Dica:**

Leia atentamente o código fornecido para entender a lógica e como os botões estão sendo configurados. Explore as funções como `digitar`, `operador`, `operacao`, e `botoes_op` para implementar a solução completa.
