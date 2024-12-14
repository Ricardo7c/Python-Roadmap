# Python-Poo
Exercícios de Programação com Classes em Python gerados pelo chat GPT

## 1. Criando uma Classe Simples

Crie uma classe chamada `Cachorro` com os seguintes atributos:

- `nome` (tipo: string)
- `idade` (tipo: inteiro)

A classe deve ter um método chamado `latir` que imprime "Au Au!".

**Tarefa**: Crie uma instância da classe `Cachorro` com o nome "Rex" e a idade 3. Em seguida, chame o método `latir`.

## 2. Classe com Método de Inicialização

Crie uma classe chamada `Retângulo` com os atributos:

- `largura` (tipo: float)
- `altura` (tipo: float)

A classe deve ter um método chamado `calcular_area` que retorna a área do retângulo.

**Tarefa**: Crie uma instância de `Retângulo` com largura 5 e altura 10. Em seguida, calcule e imprima a área.

## 3. Classe com Métodos e Atributos

Crie uma classe chamada `Carro` com os atributos:

- `marca` (tipo: string)
- `modelo` (tipo: string)
- `ano` (tipo: inteiro)
- `velocidade` (tipo: inteiro, inicia em 0)

A classe deve ter os seguintes métodos:

- `acelerar`: aumenta a velocidade em 10 unidades.
- `frear`: diminui a velocidade em 10 unidades, sem deixar a velocidade ficar negativa.

**Tarefa**: Crie uma instância de `Carro` e simule o carro acelerando duas vezes e freando uma vez. Imprima a velocidade atual após cada ação.

## 4. Classe com Atributos Privados

Crie uma classe chamada `ContaBancaria` com os atributos:

- `__saldo` (privado, tipo: float, inicia em 0)

A classe deve ter os seguintes métodos:

- `depositar(valor)`: adiciona `valor` ao saldo.
- `sacar(valor)`: subtrai `valor` do saldo se houver saldo suficiente.
- `exibir_saldo`: imprime o saldo atual.

**Tarefa**: Crie uma instância de `ContaBancaria`, faça um depósito de 100, saque 30 e exiba o saldo final.

## 5. Classe com Método de Representação

Crie uma classe chamada `Produto` com os seguintes atributos:

- `nome` (tipo: string)
- `preco` (tipo: float)

A classe deve ter um método chamado `aplicar_desconto` que recebe um percentual e reduz o preço do produto de acordo com o percentual fornecido. Além disso, crie um método `__str__` que retorne uma representação em string do produto no formato "Nome: {nome}, Preço: {preco}".

**Tarefa**: Crie uma instância da classe `Produto`, aplique um desconto e imprima a representação em string do produto.

## 6. Herança Simples

Crie uma classe base chamada `Animal` com o atributo:

- `nome` (tipo: string)

A classe deve ter um método chamado `fazer_som` que imprime "Som do animal".

Crie uma classe derivada chamada `Gato` que herda de `Animal`. A classe `Gato` deve sobrescrever o método `fazer_som` para imprimir "Miau".

**Tarefa**: Crie uma instância de `Gato` e chame o método `fazer_som`.

## 7. Contador de Instâncias

Crie uma classe chamada `Pessoa` com os atributos:

- `nome` (tipo: string)
- `idade` (tipo: inteiro)

A classe deve ter um atributo de classe chamado `contador` que conta o número de instâncias criadas.

A classe deve ter um método chamado `informar_total_pessoas` que retorna o número total de instâncias criadas.

**Tarefa**: Crie algumas instâncias de `Pessoa`, e chame o método `informar_total_pessoas` para verificar o número total de pessoas.

## 8. Comparação de Objetos

Crie uma classe chamada `Livro` com os atributos:

- `titulo` (tipo: string)
- `autor` (tipo: string)
- `ano_publicacao` (tipo: inteiro)

A classe deve ter um método `__eq__` que permite comparar dois livros para verificar se são iguais com base no título e autor.

**Tarefa**: Crie duas instâncias de `Livro` e compare-as para verificar se são iguais.

## 9. Classe com Métodos de Classe e Estáticos

Crie uma classe chamada `Matematica` com o seguinte método de classe e método estático:

- **Método de Classe**: `fatorial(n)`, que calcula o fatorial de um número `n`.
- **Método Estático**: `multiplicar(a, b)`, que retorna o produto de dois números `a` e `b`.

**Tarefa**: Crie uma instância da classe `Matematica`, use o método de classe `fatorial` para calcular o fatorial de 5 e use o método estático `multiplicar` para multiplicar 4 e 6. Imprima os resultados.

## 10. Classe com Propriedades

Crie uma classe chamada `Pessoa` com os seguintes atributos:

- `nome` (tipo: string)
- `idade` (tipo: inteiro)

A classe deve ter uma propriedade `categoria` que retorna:

- "Menor de idade" se a idade for menor que 18
- "Adulto" se a idade for 18 ou maior

**Tarefa**: Crie uma instância da classe `Pessoa` com uma idade de sua escolha e imprima a categoria da pessoa usando a propriedade `categoria`.

## 11. Sistema de Funcionários

Crie uma classe chamada `Funcionario` com os seguintes atributos:

- `nome` (tipo: string)
- `cargo` (tipo: string)
- `salario` (tipo: float)

A classe deve ter um método chamado `aumentar_salario` que recebe uma porcentagem e aumenta o salário do funcionário de acordo com essa porcentagem.

Em seguida, crie uma subclasse chamada `Gerente` que herda de `Funcionario` e adiciona um atributo `bonus` ao salário base. Implemente o método `aumentar_salario` na classe `Gerente` de forma que ele inclua o bônus no cálculo.

**Tarefa:** Crie instâncias das classes `Funcionario` e `Gerente`, aplique aumentos salariais e exiba os novos salários.

## 12. Sistema de Pedidos

Crie uma classe chamada `Produto` com os seguintes atributos:

- `nome` (tipo: string)
- `preco` (tipo: float)

Crie uma classe chamada `Pedido` que possa conter vários produtos. A classe deve ter métodos para adicionar produtos ao pedido, calcular o valor total do pedido, e remover um produto específico do pedido.

**Tarefa:** Crie instâncias de `Produto` e adicione-as a um `Pedido`. Calcule o valor total do pedido e remova um produto, recalculando o total após a remoção.

## 13. Biblioteca

Crie uma classe chamada `Livro` com os seguintes atributos:

- `titulo` (tipo: string)
- `autor` (tipo: string)
- `ano_publicacao` (tipo: int)

Implemente uma classe chamada `Biblioteca` que gerencie uma lista de livros. A classe deve ter métodos para adicionar, remover, e buscar livros pelo título ou autor. A busca deve ser case-insensitive.

**Tarefa:** Crie uma instância da classe `Biblioteca`, adicione alguns livros, e faça buscas por título e autor, exibindo os resultados.

## 14. Sistema de Reservas

Crie uma classe chamada `Quarto` com os seguintes atributos:

- `numero` (tipo: int)
- `tipo` (tipo: string)
- `preco_por_noite` (tipo: float)

Crie uma classe chamada `Reserva` que associe um quarto a um cliente, com métodos para calcular o custo total da reserva com base no número de noites. Adicione a funcionalidade de verificar a disponibilidade de um quarto antes de efetuar uma reserva.

**Tarefa:** Crie instâncias de `Quarto` e `Reserva`, verificando a disponibilidade e calculando o custo total de uma reserva.

## 15. Sistema de Controle de Estoque

Crie uma classe chamada `ItemEstoque` com os seguintes atributos:

- `nome` (tipo: string)
- `quantidade` (tipo: int)
- `preco_por_unidade` (tipo: float)

Implemente uma classe chamada `Estoque` que gerencie uma lista de itens. A classe deve ter métodos para adicionar, remover, atualizar a quantidade de um item, e calcular o valor total do estoque. Adicione um método para buscar itens com estoque baixo (quantidade menor que um valor especificado).

**Tarefa:** Crie instâncias de `ItemEstoque`, adicione-as ao `Estoque`, e calcule o valor total do estoque. Busque por itens com estoque baixo.

## 16. Sistema de Transações Bancárias

Crie uma classe chamada `ContaBancaria` com os seguintes métodos:

- `depositar` (tipo: float)
- `sacar` (tipo: float)
- `exibir_saldo`

Implemente uma subclasse chamada `ContaPoupanca` que adiciona a funcionalidade de aplicar juros ao saldo. A taxa de juros deve ser especificada no momento da criação da conta, e deve haver um método `aplicar_juros` que atualiza o saldo com base nessa taxa.

**Tarefa:** Crie instâncias de `ContaBancaria` e `ContaPoupanca`, realize operações de depósito e saque, e aplique juros na conta poupança.

## 17. Sistema de Gestão de Tarefas

Crie uma classe chamada `Tarefa` com os seguintes atributos:

- `descricao` (tipo: string)
- `concluida` (tipo: boolean)

Adicione métodos para marcar a tarefa como concluída e para alterar a descrição da tarefa. Crie uma classe `ListaDeTarefas` que gerencie uma lista de tarefas, com métodos para adicionar, remover, listar todas as tarefas, e listar apenas as tarefas concluídas.

**Tarefa:** Crie instâncias de `Tarefa` e adicione-as à `ListaDeTarefas`. Marque algumas tarefas como concluídas e exiba a lista de tarefas concluídas.

## 18. Sistema de Agenda de Contatos

Crie uma classe chamada `Contato` com os seguintes atributos:

- `nome` (tipo: string)
- `telefone` (tipo: string)
- `email` (tipo: string)

Crie uma classe `Agenda` que gerencie uma lista de contatos, com métodos para adicionar, remover, e buscar contatos. Adicione um método para listar todos os contatos em ordem alfabética pelo nome.

**Tarefa:** Crie instâncias de `Contato` e adicione-as à `Agenda`. Busque por contatos e exiba a lista de contatos ordenada alfabeticamente.
