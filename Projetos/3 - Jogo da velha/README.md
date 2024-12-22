# Implementação do Jogo da Velha com Interface Gráfica Tkinter

**Objetivo:**  
Desenvolver um jogo da velha funcional utilizando a biblioteca `tkinter` para criar uma interface gráfica. Este exercício explora conceitos de manipulação de widgets, eventos e lógica de jogo.

---

## **Requisitos do Programa**

1. **Interface do Jogo:**
   - A janela do jogo deve conter:
     - Uma grade 3x3 de botões que representam as células do tabuleiro.
     - Um rótulo (`Label`) indicando qual jogador deve realizar a próxima jogada ou exibindo o resultado final.

2. **Regras do Jogo:**
   - O jogador "X" inicia o jogo.
   - Jogadores alternam-se para preencher as células clicando nos botões.
   - Um jogador vence se conseguir preencher três células consecutivas com o mesmo símbolo em uma linha, coluna ou diagonal.
   - O jogo termina em empate se todas as células forem preenchidas sem que haja um vencedor.

3. **Funcionalidades:**
   - Os botões devem exibir "X" ou "O" conforme o jogador atual e ficar desativados após serem clicados.
   - Quando houver um vencedor ou empate, desative todos os botões restantes e exiba a mensagem correspondente no rótulo:
     - Exemplo: "X venceu!" ou "Empate!".
   - A lógica de verificação deve avaliar todas as combinações vencedoras (linhas, colunas e diagonais).

---

## **Descrição do Funcionamento**

1. **Inicialização:**
   - Configure a janela principal do jogo com dimensões fixas, título e widgets necessários.
   - Crie os botões em uma lista para facilitar o acesso e organize-os em uma grade 3x3.

2. **Eventos:**
   - Implemente uma função para tratar o clique em cada botão. Esta função deve:
     - Atualizar o símbolo do botão conforme o jogador atual.
     - Alternar a vez entre os jogadores.
     - Verificar se há um vencedor ou empate.
   - Crie uma função separada para verificar combinações vencedoras e, caso necessário, finalizar o jogo.

3. **Finalização do Jogo:**
   - Desative todos os botões ao término do jogo.
   - Atualize o rótulo para exibir o resultado.

---

## **Exemplo de Fluxo de Jogo**

1. O programa inicia com a mensagem "X começa".
2. O jogador "X" clica em uma célula, que exibe "X" e é desativada.
3. A mensagem é atualizada para "Vez do O".
4. O processo alterna entre os jogadores até:
   - Um jogador formar três símbolos consecutivos, exibindo "X venceu!" ou "O venceu!".
   - Ou todas as células serem preenchidas, exibindo "Empate!".

---

## **Objetivo Educacional**

Este exercício desenvolve habilidades em:

- Criação de interfaces gráficas com `tkinter`.
- Manipulação de eventos e widgets.
- Implementação de lógica condicional para verificar combinações vencedoras.
- Planejamento e organização do código em funções.

Teste sua solução para garantir que o jogo funciona corretamente e que a interface está intuitiva para o usuário.
