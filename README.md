# API Sistema de Pagamentos

Projeto desenvolvido com Django REST Framework utilizando Celery e Redis para processamento das notificações.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- SQLite

---

# Objetivo do Projeto

O sistema permite:

- Cadastro de clientes
- Cadastro de produtos
- Cadastro de preços
- Criação automática de notificações
- Processamento assíncrono utilizando Celery

O objetivo é demonstrar a integração entre APIs REST e filas assíncronas em um ambiente backend profissional.

---

# Estrutura do Projeto

```bash
sistema_pagamentos/
│
├── config/
├── vendas/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Funcionalidades

## Clientes
Permite cadastrar clientes no sistema.

## Produtos
Permite cadastrar produtos.

## Preços
Permite registrar preços relacionados aos clientes e produtos.

## Notificações
As notificações são criadas automaticamente através do Celery após o cadastro de um preço.

---

# Instalação do Projeto

## 1. Clonar repositório

```bash
git clone https://github.com/AndressasAntunes/API-sistema_pagamentos.git
```

---

## 2. Entrar na pasta

```bash
cd API-sistema_pagamentos
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Executando o Projeto

## Rodar servidor Django

```bash
python manage.py runserver
```

Servidor:

```text
http://127.0.0.1:8000/
```

---

# Redis com Docker

Executar Redis:

```bash
docker run -p 6379:6379 redis
```

---

# Executar Celery

```bash
python -m celery -A config worker --pool=solo --loglevel=info
```

---

# Rotas da API

## Clientes

```text
/api/clientes/
```

## Produtos

```text
/api/produtos/
```

## Preços

```text
/api/precos/
```

## Notificações

```text
/api/notificacoes/
```

---

# Exemplo de Requisição

## POST /api/precos/

```json
{
    "cliente": 1,
    "produto": 1,
    "valor": 99.90
}
```

---

# Painel Administrativo

Acesse:

```text
http://127.0.0.1:8000/admin
```

---

# Autor

Projeto desenvolvido por Andressa dos Santos Antunes para fins acadêmicos e aprendizado de desenvolvimento backend com Django e processamento assíncrono.
