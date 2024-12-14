# Bibliotecas e Arquivos

Aqui estão 10 exercícios sobre o tema **Uso de Bibliotecas** em Python, abrangendo os tópicos que você mencionou:

## 1. Importação de Bibliotecas Padrão

- **Objetivo**: Importe a biblioteca `math` e use a função `sqrt` para calcular a raiz quadrada de um número.
- **Instruções**:
  - Importe a biblioteca `math`.
  - Crie uma função que recebe um número como parâmetro e retorna sua raiz quadrada.
  - Teste a função com diferentes números.

## 2. Instalando Bibliotecas Externas com `pip`

- **Objetivo**: Instale a biblioteca externa `requests` usando o `pip`.
- **Instruções**:
  - Use o comando pip para instalar a biblioteca requests.
  - Após a instalação, importe a biblioteca.
  - Faça uma requisição HTTP GET para a API do GitHub para obter informações sobre um repositório público. Por exemplo: https://api.github.com/repos/Ricardo7c/Python-Roadmap
  - Exiba o conteúdo da resposta da requisição em formato JSON.
    *(Nota: Se você já tem a biblioteca instalada, basta realizar o código).*

## 3. Escrita de Arquivos

- **Objetivo**: Crie um arquivo de texto, escreva nele uma lista de nomes.

- **Instruções**:
  - Crie uma lista de nomes.
  - Abra um arquivo de texto no modo de escrita com `with open()`
  - Escreva os nomes no arquivo.

## 4. Leitura de Arquivos

- **Objetivo**: Leia o arquivo de texto criado no exercicio anterior.
- **Instruções**:
  - Abra o arquivo no modo de leitura.
  - Exiba o conteúdo do arquivo linha por linha.

## 5. Manipulação de Diretórios com `os`

- **Objetivo**: Crie e remova um diretório usando a biblioteca `os`.
- **Instruções**:
  - Importe a biblioteca `os`.
  - Crie um novo diretório.

## 6. Criação de arquivo JSON

- **Objetivo**: Criar arquivo JSON.
- **Instruções**:
  - Crie um dicionario python com nome e idade de uma pessoa
  - Escreva em um arquivo.json usando o metodo `dumps()` para formatar.

## 7. Leitura de arquivo JSON

- **Objetivo**: Leia o arquivo JSON criado no exercicio anterior
- **Instruções**:
  - Abra o arquivo JSON e convertar de volta para dicionario usando o metodo `load()`
  - Exiba os dados do dicionario

## 8. Listando Arquivos em um Diretório

- **Objetivo**: Liste todos os arquivos de um diretório específico usando `os`.
- **Instruções**:
  - Importe a biblioteca `os`.
  - Liste todos os arquivos presentes em um diretório especificado.
  - Exiba o nome de cada arquivo.

## 9. Criação de CSV

- **Objetivo**: Escreva dados em um arquivo CSV utilizando a biblioteca `csv`.
- **Instruções**:
  - Inporte a biblioteca `csv`
  - Crie um `arquivo.csv` no modo de escrita `"w"`
  - Crie um novo escritor para o arquivo com o metodo `writer()`
  - Escreva o cabeçalho e as linhas no csv com o metodo `writerow()`

## 10. Leitura de CSV

- **Objetivo**: Leia os dados em um arquivo CSV utilizando a biblioteca `csv`.
- **Instruções**:
  - Abra o arquivo csv no motod leitura
  - Use a biblioteca `csv` para ler o arquivo e exibir seus conteúdos.
