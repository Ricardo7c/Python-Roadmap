# **Poetry**

## **Exercício 1 - Criar um Projeto com Poetry**

**Objetivo:** Aprender a inicializar um projeto com Poetry.

**Instruções:**

1. Crie uma nova pasta para seu projeto: `poetry_exercicio1`
2. Dentro dela, execute:

   ```bash
   poetry init
   ```

   ou diretamente:

   ```bash
   poetry new conversor_temperatura
   ```

**Desafio:**
Implemente um script simples em `conversor_temperatura` que converta graus Celsius para Fahrenheit.
Exemplo de entrada: `25`
Saída esperada: `25°C = 77°F`

---

## **Exercício 2 - Adicionar Dependências**

**Objetivo:** Aprender a adicionar e remover pacotes usando o Poetry.

**Instruções:**

1. Dentro do projeto anterior, adicione a biblioteca `click` com:

   ```bash
   poetry add click
   ```

2. Crie um CLI com `click` para pedir a temperatura e imprimir o resultado da conversão.

**Desafio bônus:**
Remova a biblioteca `click` com:

```bash
poetry remove click
```

---

## **Exercício 3 - Trabalhar com o ambiente virtual**

**Objetivo:** Usar o ambiente virtual gerenciado pelo Poetry.

**Instruções:**

1. Ative o ambiente:

   ```bash
   poetry shell
   ```

2. Rode seu script dentro desse ambiente:

   ```bash
   python conversor_temperatura/main.py
   ```

3. Saia com `exit`

**Desafio:**
Descubra o caminho do ambiente virtual com:

```bash
poetry env info --path
```

---

## **Exercício 4 - Empacotar o Projeto**

**Objetivo:** Aprender a empacotar um projeto para distribuição.

**Instruções:**

1. Edite o arquivo `pyproject.toml` e preencha as seções `[tool.poetry]` com:

   * name
   * version
   * description
   * authors
   * license

2. Gere o pacote:

   ```bash
   poetry build
   ```

**Desafio:**
Liste os arquivos gerados dentro da pasta `dist`.

---

## **Exercício 5 - Publicar em TestPyPI**

**Objetivo:** Praticar a publicação de pacotes.

**Instruções:**

1. Crie uma conta em [https://test.pypi.org/](https://test.pypi.org/)

2. Gere um token de API.

3. Configure o repositório com:

   ```bash
   poetry config repositories.testpypi https://test.pypi.org/legacy/
   poetry config pypi-token.testpypi <SEU_TOKEN>
   ```

4. Publique com:

   ```bash
   poetry publish -r testpypi
   ```

**Desafio:**
Tente instalar seu próprio pacote com:

```bash
pip install --index-url https://test.pypi.org/simple seu-pacote
```

---

## **Exercício 6 - Usar Dependências Dev**

**Objetivo:** Instalar pacotes apenas para desenvolvimento.

**Instruções:**

1.Adicione `pytest` como dependência de desenvolvimento:

   ```bash
   poetry add --group dev pytest
   ```

2.Crie um teste em `tests/test_conversor.py`:

```python
from conversor_temperatura.main import celsius_para_fahrenheit

def test_convert_25():
    assert celsius_para_fahrenheit(25) == 77
```

3.Rode os testes com:

```bash
poetry run pytest
```
