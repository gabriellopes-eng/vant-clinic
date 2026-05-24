# VANT Clinic

Backend em Django para gestao de clinicas de estetica.

## Comandos finais (Etapa 14)

Execute os comandos abaixo na raiz do projeto.

### 1. Ativar ambiente virtual

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Garantir dependencias instaladas

```powershell
python -m pip install -r requirements.txt
```

### 3. Gerar e aplicar migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar usuario administrador

```powershell
python manage.py createsuperuser
```

### 5. Rodar servidor

```powershell
python manage.py runserver
```

### 6. Rotas principais para teste

- /
- /admin/
- /clientes/
- /profissionais/
- /servicos/
- /agendamentos/
- /pagamentos/
- /relatorios/resumo/