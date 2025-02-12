# Jogo da Forca

## Objetivo

Criar um programa interativo em Python que simule o clássico **Jogo da Forca**. O jogo deve permitir que um jogador tente adivinhar uma palavra secreta fornecida pelo programa, utilizando conceitos de **laços de repetição** e **estruturas condicionais**. O jogo termina quando o jogador adivinhar corretamente a palavra ou esgotar o número máximo de tentativas.

---

## Instruções

1. **Descrição do jogo**:
   - O jogo consiste em adivinhar uma palavra secreta, letra por letra.
   - O jogador tem um número limitado de tentativas para acertar a palavra.
   - A cada tentativa, o jogador insere uma letra, e o programa verifica se ela está na palavra secreta:
     - **Se a letra estiver presente**: ela é revelada nas posições corretas.
     - **Se a letra não estiver presente**: o número de tentativas restantes é reduzido.

2. **Regras**:
   - O programa deve armazenar uma palavra secreta definida previamente (ou escolhida aleatoriamente de uma lista de palavras).
   - O jogador pode tentar adivinhar letras uma de cada vez.
   - O jogador não pode repetir a mesma letra já tentada:
     - Se isso ocorrer, o programa deve exibir uma mensagem de alerta e não descontar uma tentativa.
   - O jogador vence se acertar todas as letras da palavra antes de esgotar as tentativas.
   - O jogador perde se errar mais vezes do que o número máximo de tentativas permitidas.

3. **Requisitos do programa**:
   - Utilizar **laços de repetição** para continuar o jogo enquanto ele estiver ativo.
   - Utilizar **condicionais** para verificar as tentativas e validar as letras inseridas.
   - O jogo deve exibir mensagens claras, como:
     - O estado atual da palavra `(ex: "_ _ a _ a")`.
     - O número de tentativas restantes.
     - Uma lista de letras já utilizadas.
     - Mensagens indicando vitória ou derrota.

4. **Entrada e saída esperada**:
   - O jogador insere uma letra por vez.
   - O programa exibe:
     - O progresso atual da palavra (com letras descobertas e os espaços ainda ocultos).
     - As tentativas restantes.
     - Um aviso se o jogador tentar uma letra já utilizada.

---

## Exemplo de saída esperada

**Palavra secreta**: `banana`

1. **Início do jogo**:

   ```powershell
   Bem-vindo ao Jogo da Forca!
   A palavra secreta tem 6 letras.
   _ _ _ _ _ _
   Você tem 6 tentativas restantes.
   ```

2. **Primeira tentativa** (entrada: `a`):

   ```powershell
   Você acertou! A letra 'a' está na palavra.
   _ a _ a _ a
   Letras usadas: a
   Tentativas restantes: 6
   ```

3. **Segunda tentativa** (entrada: `z`):

   ```powershell
   A letra 'z' não está na palavra.
   _ a _ a _ a
   Letras usadas: a, z
   Tentativas restantes: 5
   ```

4. **Terceira tentativa** (entrada: `b`):

   ```powershell
   Você acertou! A letra 'b' está na palavra.
   b a _ a _ a
   Letras usadas: a, z, b
   Tentativas restantes: 5
   ```

5. **Fim do jogo**:

   - **Caso vença**:

    ```powershell
    Parabéns! Você descobriu a palavra: banana.
    ```

   - **Caso perca**:

    ```powershell
    Que pena! Você perdeu. A palavra era banana.
    ```

---

## Extensões opcionais

- Permitir ao jogador escolher o nível de dificuldade (variando o número de tentativas).
- Implementar uma lista de palavras aleatórias para o programa selecionar.
- Permitir ao jogador tentar adivinhar a palavra completa em vez de apenas uma letra por vez.

---

## Observação

Implemente o jogo com código limpo, utilizando comentários para descrever a lógica e testando todas as possibilidades (vitória, derrota, tentativas repetidas). Divirta-se programando!
