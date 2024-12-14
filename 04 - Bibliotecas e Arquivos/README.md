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

- **Objetivo**: Crie um arquivo de texto, escreva nele uma lista de nomes e depois feche o arquivo da forma tradicional com open() e close().
- **Instruções**:
  - Crie uma lista de nomes.
  - Abra um arquivo de texto no modo de escrita.
  - Escreva os nomes no arquivo.
  - Feche o arquivo ao final.

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
  - Liste o conteúdo do diretório para verificar se foi criado corretamente.
  - Remova o diretório criado.

## 6. Leitura de Arquivo JSON

- **Objetivo**: Leia um arquivo JSON e exiba seu conteúdo.
- **Instruções**:
  - Crie um arquivo JSON com alguns dados simples (por exemplo, um objeto com nome e idade).
  - Use a biblioteca `json` para carregar e exibir os dados do arquivo.

## 7. Listando Arquivos em um Diretório

- **Objetivo**: Liste todos os arquivos de um diretório específico usando `os`.
- **Instruções**:
  - Importe a biblioteca `os`.
  - Liste todos os arquivos presentes em um diretório especificado.
  - Exiba o nome de cada arquivo.

## 8. Manipulando Arquivos CSV

- **Objetivo**: Leia e escreva dados em um arquivo CSV utilizando a biblioteca `csv`.
- **Instruções**:
  - Crie um arquivo CSV contendo algumas informações, como nome, idade e cidade.
  - Use a biblioteca `csv` para ler o arquivo e exibir seus conteúdos.
  - Crie uma nova entrada e adicione ao arquivo CSV.

## 9. Instalação de Bibliotecas com Dependências

- **Objetivo**: Instale a biblioteca `pandas` e utilize-a para criar um DataFrame simples.
- **Instruções**:
  - Instale a biblioteca `pandas` usando o comando `pip`.
  - Após a instalação, crie um DataFrame simples com algumas colunas e exiba o conteúdo.
  - Teste a manipulação de dados com o DataFrame (ex.: seleção de colunas).

## 10. Usando `shutil` para Copiar Arquivos

- **Objetivo**: Copie um arquivo de um diretório para outro utilizando a biblioteca `shutil`.
- **Instruções**:
  - Crie dois diretórios (origem e destino).
  - Crie um arquivo em um dos diretórios.
  - Use `shutil.copy()` para copiar o arquivo para o outro diretório.
  - Verifique se o arquivo foi copiado corretamente.

---
