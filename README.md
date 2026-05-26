# VANT Clinic

<p align="left">
	<img src="https://img.shields.io/badge/Django-6.0.5-6F42C1?style=for-the-badge&labelColor=2B0E52" alt="Django 6.0.5">
	<img src="https://img.shields.io/badge/Python-3.13-8F63D6?style=for-the-badge&labelColor=2B0E52" alt="Python 3.13">
	<img src="https://img.shields.io/badge/Status-Ativo-7A3FF2?style=for-the-badge&labelColor=2B0E52" alt="Status Ativo">
</p>

Plataforma web para operacao de clinicas de estetica, com foco em agenda, atendimento, pagamentos e visao de indicadores.

## Visao geral

O projeto foi construido em Django com arquitetura modular por app:

- `clientes`: cadastro e manutencao de clientes.
- `profissionais`: equipe, especialidades e status.
- `servicos`: catalogo de procedimentos, duracao e preco.
- `agendamentos`: agenda com regra de conflito por profissional e horario.
- `pagamentos`: controle financeiro por agendamento.
- `relatorios`: resumo operacional e financeiro.

## Destaques funcionais

- Frontend responsivo com identidade visual roxa e layout SaaS.
- Autenticacao de usuario comum (`login`, `logout`, `cadastro`).
- Rotas de negocio protegidas por login.
- Regra critica de agenda: impede dois agendamentos ativos no mesmo horario para o mesmo profissional.
- Relatorio consolidado com totais de operacao e valor pago.

## Stack

- Python + Django
- SQLite (desenvolvimento)
- Templates Django + CSS/JS proprio

## Quick start

Execute os comandos abaixo na raiz do projeto.

### 1. Ativar ambiente virtual (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 3. Aplicar migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar usuario administrador (opcional, recomendado)

```powershell
python manage.py createsuperuser
```

### 5. Subir aplicacao

```powershell
python manage.py runserver
```

Aplicacao: `http://127.0.0.1:8000/`

## Autenticacao

Fluxo para usuario comum:

- Cadastro: `/auth/register/`
- Login: `/auth/login/`
- Logout: `/auth/logout/`

Rotas de modulo exigem autenticacao. Sem login, o usuario e redirecionado automaticamente para a tela de login.

## Rotas principais

- `/`
- `/admin/`
- `/clientes/`
- `/profissionais/`
- `/servicos/`
- `/agendamentos/`
- `/pagamentos/`
- `/relatorios/resumo/`

## Regra de negocio importante

No modulo de agendamentos, o sistema valida conflito de horario ativo por profissional. Em outras palavras:

- se ja existe um agendamento ativo para o profissional no horario X, outro nao pode ser criado no mesmo slot;
- se o agendamento anterior for cancelado, o slot volta a ficar disponivel.

## Qualidade e verificacao

Rodar validacao geral:

```powershell
python manage.py check
```

Validacao rapida de rotas (opcional):

```powershell
python manage.py shell -c "from django.test import Client; c=Client(); urls=['/','/clientes/','/profissionais/','/servicos/','/agendamentos/','/pagamentos/','/relatorios/resumo/']; print({u:c.get(u, HTTP_HOST='localhost').status_code for u in urls})"
```

## Estrutura resumida

```text
config/           # settings e urls globais
core/             # home, autenticacao e base layout
clientes/         # CRUD de clientes
profissionais/    # CRUD de profissionais
servicos/         # CRUD de servicos
agendamentos/     # agenda e cancelamento
pagamentos/       # CRUD de pagamentos
relatorios/       # dashboards e resumo
```

## Observacao de ambiente

Este projeto esta pronto para desenvolvimento local. Para producao, recomenda-se:

- banco gerenciado (PostgreSQL),
- configuracao de `ALLOWED_HOSTS`,
- secret key por variavel de ambiente,
- servidor WSGI/ASGI dedicado.