# VANT Clinic

<p align="left">
	<img src="https://img.shields.io/badge/Django-6.0.5-6F42C1?style=for-the-badge&labelColor=2B0E52" alt="Django 6.0.5">
	<img src="https://img.shields.io/badge/Python-3.13-8F63D6?style=for-the-badge&labelColor=2B0E52" alt="Python 3.13">
	<img src="https://img.shields.io/badge/Status-Active-7A3FF2?style=for-the-badge&labelColor=2B0E52" alt="Status Active">
</p>

Web platform for aesthetic clinic operations, focused on scheduling, service delivery, payments, and performance visibility.

<img width="1365" height="621" alt="image" src="https://github.com/user-attachments/assets/5401d7df-b7bb-4d47-abbc-dbabcaf58bb0" />

## Overview

The project was built with Django using a modular app-based architecture:

- `clientes`: client registration and maintenance.
- `profissionais`: team members, specialties, and status.
- `servicos`: procedure catalog, duration, and pricing.
- `agendamentos`: scheduling with conflict validation per professional and time slot.
- `pagamentos`: payment control per appointment.
- `relatorios`: operational and financial summary.

## Functional highlights

- Responsive frontend with a purple visual identity and SaaS-style layout.
- Regular user authentication (`login`, `logout`, `register`).
- Business routes protected by authentication.
- Critical scheduling rule: blocks two active appointments at the same time for the same professional.
- Consolidated report with operational totals and total paid amount.

## Stack

- Python + Django
- SQLite (development)
- Django templates + custom CSS/JS

## Quick start

Run the commands below from the project root.

### 1. Activate virtual environment (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Apply migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create admin user (optional, recommended)

```powershell
python manage.py createsuperuser
```

### 5. Run the application

```powershell
python manage.py runserver
```

Application: `http://127.0.0.1:8000/`

## Authentication

Regular user flow:

- Register: `/auth/register/`
- Login: `/auth/login/`
- Logout: `/auth/logout/`

Module routes require authentication. Without login, users are automatically redirected to the login page.

## Main routes

- `/`
- `/admin/`
- `/clientes/`
- `/profissionais/`
- `/servicos/`
- `/agendamentos/`
- `/pagamentos/`
- `/relatorios/resumo/`

## Important business rule

In the scheduling module, the system validates active time conflicts per professional. In other words:

- if there is already an active appointment for a professional at time X, another appointment cannot be created in the same slot;
- if the previous appointment is cancelled, the slot becomes available again.

## Quality and verification

Run general validation:

```powershell
python manage.py check
```

Quick route validation (optional):

```powershell
python manage.py shell -c "from django.test import Client; c=Client(); urls=['/','/clientes/','/profissionais/','/servicos/','/agendamentos/','/pagamentos/','/relatorios/resumo/']; print({u:c.get(u, HTTP_HOST='localhost').status_code for u in urls})"
```

## Project structure (summary)

```text
config/           # global settings and urls
core/             # home, authentication, and base layout
clientes/         # client CRUD
profissionais/    # professional CRUD
servicos/         # service CRUD
agendamentos/     # scheduling and cancellation
pagamentos/       # payment CRUD
relatorios/       # dashboards and summary
```

## Environment note

This project is ready for local development. For production, it is recommended to use:

<<<<<<< HEAD
- managed database (PostgreSQL),
- proper `ALLOWED_HOSTS` configuration,
- secret key via environment variable,
- dedicated WSGI/ASGI server.
=======
- banco gerenciado (PostgreSQL),
- configuracao de `ALLOWED_HOSTS`,
- secret key por variavel de ambiente,
- servidor WSGI/ASGI dedicado.
>>>>>>> 5affde3a1adf0a53ebf075337456d9509bcba4dc
