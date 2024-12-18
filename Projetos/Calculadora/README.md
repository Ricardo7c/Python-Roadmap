# Projeto 1. Calculadora Simples em Python  

**Objetivo:**  
Criar uma calculadora simples em Python que permita ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão). A calculadora deve ser interativa, aceitar entrada do usuário e exibir o resultado da operação escolhida.

---

## Instruções  

1. **Definição do programa:**  
   O programa deve:
   - Solicitar ao usuário qual operação deseja realizar.
   - Aceitar dois números como entrada.
   - Realizar a operação selecionada.
   - Exibir o resultado ao usuário.

2. **Operações obrigatórias:**  
   - Adição (`+`)
   - Subtração (`-`)
   - Multiplicação (`*`)
   - Divisão (`/`)

3. **Requisitos:**  
   - Validação de entrada:
     - Se o usuário inserir algo que não seja um número, exibir uma mensagem de erro e pedir novamente.
     - Caso o usuário escolha divisão, garantir que o divisor não seja zero.
   - O programa deve continuar solicitando operações até que o usuário escolha sair.
   - Deve haver uma opção clara para encerrar o programa (exemplo: digitando `sair`).

4. **Estrutura do código:**  
   - Utilize funções para organizar o programa:
     - Uma função para cada operação matemática.
     - Uma função para exibir o menu de opções.
     - Uma função principal para controlar o fluxo do programa.
   - Opte por boas práticas, como comentários explicativos e nomes de variáveis autoexplicativos.

5. **Extras (opcional):**  
   - Adicionar mais operações como potênciação (`**`), resto da divisão (`%`) e raiz quadrada.
   - Permitir cálculos com múltiplos números (exemplo: soma de uma lista de números).
   - Exibir um histórico de operações realizadas.

---

## Exemplo de saída esperada  

```plaintext
Bem-vindo à Calculadora Simples!
Escolha uma operação:
1. Adição (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Sair
Digite sua escolha: 1

Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 10 + 5 = 15

Escolha uma operação:
1. Adição (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Sair
Digite sua escolha: 4

Digite o primeiro número: 10
Digite o segundo número: 0
Erro: Não é possível dividir por zero. Tente novamente.

Escolha uma operação:
1. Adição (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Sair
Digite sua escolha: 5
Encerrando a calculadora. Obrigado por usar!
```

---
