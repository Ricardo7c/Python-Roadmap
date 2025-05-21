# **Virtualenv (pip + venv)**

Aprender a:

* Criar ambientes isolados com `virtualenv`
* Ativar/desativar ambientes
* Instalar pacotes sem afetar o sistema
* Gerenciar o `requirements.txt`

## Criando um ambiente virtual

**Objetivo:** Criar um novo ambiente virtual com `virtualenv`.

**Instruções:**

1. Crie uma pasta chamada `ex01_virtualenv_basico`.
2. Dentro dela, crie um ambiente virtual com o nome `venv` usando `virtualenv`.
3. Ative o ambiente.
4. Verifique se o ambiente está ativo observando o prefixo no terminal.

**Dica:**

```bash
virtualenv venv
.\venv\Scripts\activate  # no CMD
# ou
.\venv\Scripts\Activate.ps1  # no PowerShell
```

## Instalando e congelando dependências

**Objetivo:** Praticar a instalação de pacotes e salvar as dependências.

**Instruções:**

1. Ative o ambiente virtual da pasta anterior.
2. Instale os seguintes pacotes:

   * `requests`
   * `colorama`
3. Gere o arquivo `requirements.txt`.

**Comandos úteis:**

```bash
pip install requests colorama
pip freeze > requirements.txt
```

## Recriando o ambiente a partir do `requirements.txt`

**Objetivo:** Aprender a reconstruir ambientes em outras máquinas ou pastas.

**Instruções:**

1. Crie uma nova pasta chamada `ex03_reinstalando`.
2. Copie o `requirements.txt` da pasta anterior para essa nova pasta.
3. Crie e ative um novo ambiente virtual com `virtualenv`.
4. Instale os pacotes com base no `requirements.txt`.

**Comandos:**

```bash
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Ambiente isolado para um mini projeto

**Objetivo:** Criar um ambiente separado para um script que usa pacotes externos.

**Instruções:**

1. Crie uma pasta chamada `ex04_projeto_github`.
2. Dentro dela, crie um ambiente virtual.
3. Escreva um script chamado `seguidores.py` que usa o pacote `followers-github` para mostrar **quem te segue de volta no GitHub**.
4. Ative o ambiente, instale `followers-github` e execute o script.

## Explorando conflitos

**Objetivo:** Entender como ambientes virtuais evitam conflitos de versões.

**Instruções:**

1. Crie duas pastas: `projeto_a` e `projeto_b`.
2. Em `projeto_a`, crie um ambiente virtual e instale `flask==1.1.2`.
3. Em `projeto_b`, crie outro ambiente virtual e instale `flask==2.2.5`.
4. Ative cada ambiente e execute `python -m flask --version` para verificar as versões instaladas.

## 💡 Extras

* Crie um script `desativar.ps1` que apenas executa `deactivate` (opcional).
* Crie um `.gitignore` e inclua o diretório `venv` para evitar subir dependências no repositório.

---
