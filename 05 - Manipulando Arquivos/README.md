# Manipulando Arquivos

## 1. Escrita de Arquivos

- **Objetivo**: Crie um arquivo de texto, escreva nele uma lista de nomes.

- **Instruções**:
  - Crie uma lista de nomes.
  - Abra um arquivo de texto no modo de escrita com `with open()`
  - Escreva os nomes no arquivo.

## 2. Leitura de Arquivos

- **Objetivo**: Leia o arquivo de texto criado no exercicio anterior.
- **Instruções**:
  - Abra o arquivo no modo de leitura.
  - Exiba o conteúdo do arquivo linha por linha.

## 3. Manipulação de Diretórios com `os`

- **Objetivo**: Crie e remova um diretório usando a biblioteca `os`.
- **Instruções**:
  - Importe a biblioteca `os`.
  - Crie um novo diretório.

## 4. Criação de arquivo JSON

- **Objetivo**: Criar arquivo JSON.
- **Instruções**:
  - Crie um dicionario python com nome e idade de uma pessoa
  - Escreva em um arquivo.json usando o metodo `dumps()` para formatar.

## 5. Leitura de arquivo JSON

- **Objetivo**: Leia o arquivo JSON criado no exercicio anterior
- **Instruções**:
  - Abra o arquivo JSON e convertar de volta para dicionario usando o metodo `load()`
  - Exiba os dados do dicionario

## 6. Listando Arquivos em um Diretório

- **Objetivo**: Liste todos os arquivos de um diretório específico usando `os`.
- **Instruções**:
  - Importe a biblioteca `os`.
  - Liste todos os arquivos presentes em um diretório especificado.
  - Exiba o nome de cada arquivo.

## 7. Criação de CSV

- **Objetivo**: Escreva dados em um arquivo CSV utilizando a biblioteca `csv`.
- **Instruções**:
  - Inporte a biblioteca `csv`
  - Crie um `arquivo.csv` no modo de escrita `"w"`
  - Crie um novo escritor para o arquivo com o metodo `writer()`
  - Escreva o cabeçalho e as linhas no csv com o metodo `writerow()`

## 8. Leitura de CSV

- **Objetivo**: Leia os dados em um arquivo CSV utilizando a biblioteca `csv`.
- **Instruções**:
  - Abra o arquivo csv no motod leitura
  - Use a biblioteca `csv` para ler o arquivo e exibir seus conteúdos.

## 9. Escrevendo dados binários em um arquivo

- **Objetivo**: Escreva um programa em Python que crie um arquivo chamado dados.bin e grave nele uma lista de números inteiros (ex: [10, 20, 30, 40, 50]) em formato binário usando o módulo struct.

Dica: Use o módulo struct com a função pack para converter os inteiros em bytes e depois escreva com 'wb'.

## 10. Lendo dados binários de um arquivo

- **Objetivo**: Crie um programa que abra o arquivo dados.bin (criado no exercício anterior) no modo binário de leitura ('rb'), leia os dados e exiba os números inteiros no console.

Dica: Use struct.unpack para converter os bytes de volta para inteiros.

## 11. Copiando um arquivo binário

- **Objetivo**: Escreva um programa que leia um arquivo binário qualquer (por exemplo, uma imagem imagem.jpg) usando o modo 'rb' e crie uma cópia exata dele chamada copia_imagem.jpg usando o modo 'wb'.

Dica: Leia e escreva em blocos de dados com tamanho fixo (ex: 1024 bytes).

## 12. Contando bytes específicos em um arquivo

- **Objetivo**: Escreva um programa que leia um arquivo binário (por exemplo, dados.bin) e conte quantas vezes um determinado byte (por exemplo, b'\x20') aparece no conteúdo.

## 13. Gravando e lendo uma string em binário

- **Objetivo**: Faça um programa que grave uma string qualquer (como "Olá, mundo!") em um arquivo binário chamado texto.bin e depois leia esse mesmo arquivo e imprima a string no console.

Dica: Use .encode() para converter a string em bytes antes de gravar, e .decode() ao ler.
