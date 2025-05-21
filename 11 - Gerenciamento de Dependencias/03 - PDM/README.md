# PDM

---

## **1 – Criando seu primeiro projeto com PDM**

**Objetivo:** aprender a inicializar um projeto com `pdm`.

**Instruções:**

1. Crie uma pasta chamada `exercicio01_pdm`.
2. Dentro dela, execute:

   ```bash
   pdm init
   ```
3. Preencha as informações interativamente (nome, versão do Python, etc).
4. Após criar o `pyproject.toml`, execute:

   ```bash
   pdm info
   ```

**Verifique se o `pyproject.toml` foi gerado corretamente.**

---

## **2 – Adicionando dependências**

**Objetivo:** praticar adição de bibliotecas e execução de código com PDM.

**Instruções:**

1. Crie um script chamado `main.py` com este conteúdo:

   ```python
   import requests

   response = requests.get("https://api.github.com")
   print(f"Status: {response.status_code}")
   ```
2. Instale a dependência:

   ```bash
   pdm add requests
   ```
3. Execute o script com:

   ```bash
   pdm run python main.py
   ```

**Resultado esperado:** deve imprimir `Status: 200`.

---

## **3 – Usando grupos de dependência**

**Objetivo:** separar dependências de desenvolvimento.

**Instruções:**

1. Adicione o Black como dependência de desenvolvimento:

   ```bash
   pdm add --group dev black
   ```
2. Verifique no `pyproject.toml` se Black está no grupo correto.
3. Rode o formatador no seu projeto:

   ```bash
   pdm run black main.py
   ```

---

## **4 – Scripts personalizados no `pyproject.toml`**

**Objetivo:** rodar scripts com nome curto usando `pdm run`.

**Instruções:**

1. Edite o `pyproject.toml` e adicione:

   ```toml
   [tool.pdm.scripts]
   rodar = "python main.py"
   ```
2. Rode o script com:

   ```bash
   pdm run rodar
   ```

**Resultado esperado:** deve executar seu `main.py`.

---

## **5 – Bloqueando dependências e exportando**

**Objetivo:** travar versões e gerar `requirements.txt`.

**Instruções:**

1. Rode:

   ```bash
   pdm lock
   ```

2. Exporte para `requirements.txt`:

   ```bash
   pdm export > requirements.txt
   ```

3. Verifique se o arquivo `requirements.txt` foi criado corretamente.
