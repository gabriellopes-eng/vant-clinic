# Relatorio de Validacao Manual - Backend VANT

Data: 24/05/2026
Objetivo: validar manualmente se o backend Django do VANT esta funcionando de ponta a ponta.

## 1. Preparacao do ambiente

No PowerShell, na raiz do projeto:

```powershell
Set-Location "c:\Users\Elward\Repositorios - Gabriel\vant-clinic"
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

Resultado esperado:
- `No changes detected` no `makemigrations`.
- `No migrations to apply` no `migrate` (ou aplicacoes pendentes, se houver).
- `System check identified no issues` no `check`.

## 2. Subir o servidor

```powershell
python manage.py runserver
```

Resultado esperado:
- servidor iniciado em `http://127.0.0.1:8000/` sem erro no terminal.

## 3. Checklist rapido de rotas

Abra no navegador:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`
- `http://127.0.0.1:8000/clientes/`
- `http://127.0.0.1:8000/profissionais/`
- `http://127.0.0.1:8000/servicos/`
- `http://127.0.0.1:8000/agendamentos/`
- `http://127.0.0.1:8000/pagamentos/`
- `http://127.0.0.1:8000/relatorios/resumo/`

Resultado esperado:
- todas as paginas carregam com status visual OK (sem tela de erro Django).

## 4. Criar superusuario (se ainda nao criou)

```powershell
python manage.py createsuperuser
```

Depois entrar no admin em `http://127.0.0.1:8000/admin/`.

Resultado esperado:
- login no admin funcionando.
- modelos visiveis: Cliente, Profissional, Servico Estetico, Agendamento, Pagamento.

## 5. Teste funcional completo (fluxo principal)

### 5.1 Clientes
1. Ir em `/clientes/`.
2. Clicar em "Novo cliente".
3. Cadastrar 1 cliente.
4. Editar cliente.
5. Excluir cliente de teste (opcional).

Resultado esperado:
- CRUD de cliente funcionando.

### 5.2 Profissionais
1. Ir em `/profissionais/`.
2. Cadastrar 1 profissional.
3. Editar profissional.

Resultado esperado:
- CRUD de profissional funcionando.

### 5.3 Servicos
1. Ir em `/servicos/`.
2. Cadastrar 1 servico com duracao e preco.
3. Editar servico.

Resultado esperado:
- CRUD de servico funcionando.

### 5.4 Agendamentos (com regra principal)
1. Ir em `/agendamentos/`.
2. Cadastrar um agendamento com:
   - Cliente A
   - Profissional X
   - Servico Y
   - Data/Hora Z
3. Tentar cadastrar outro agendamento com:
   - Outro cliente (ou o mesmo)
   - Mesmo Profissional X
   - Mesma Data/Hora Z

Resultado esperado:
- sistema deve bloquear o segundo agendamento com mensagem de conflito de horario.

4. Cancelar o primeiro agendamento (botao "Cancelar").
5. Tentar novamente cadastrar um agendamento no mesmo Profissional X e Data/Hora Z.

Resultado esperado:
- agora deve permitir (porque o anterior foi cancelado).

### 5.5 Pagamentos
1. Ir em `/pagamentos/`.
2. Criar pagamento vinculado a um agendamento.
3. Testar status `PENDENTE` e `PAGO`.
4. Editar e excluir pagamento de teste.

Resultado esperado:
- CRUD de pagamento funcionando.

### 5.6 Relatorios
1. Ir em `/relatorios/resumo/`.

Resultado esperado:
- exibir:
  - total de agendamentos
  - total de cancelamentos
  - total de servicos
  - total de pagamentos
  - valor total pago

## 6. Validacao rapida por comando (opcional)

Com o servidor parado, rode:

```powershell
python manage.py shell -c "from django.test import Client; c=Client(); urls=['/','/clientes/','/clientes/novo/','/profissionais/','/profissionais/novo/','/servicos/','/servicos/novo/','/agendamentos/','/agendamentos/novo/','/pagamentos/','/pagamentos/novo/','/relatorios/resumo/']; print({u:c.get(u, HTTP_HOST='localhost').status_code for u in urls})"
```

Resultado esperado:
- todas as rotas retornando `200`.

## 7. Registro de evidencias

Preencha este quadro ao final:

- Ambiente subiu sem erro: [ ] Sim [ ] Nao
- Admin acessivel: [ ] Sim [ ] Nao
- CRUD Clientes: [ ] Sim [ ] Nao
- CRUD Profissionais: [ ] Sim [ ] Nao
- CRUD Servicos: [ ] Sim [ ] Nao
- Agendamento com bloqueio de conflito: [ ] Sim [ ] Nao
- Cancelamento liberando novo horario: [ ] Sim [ ] Nao
- CRUD Pagamentos: [ ] Sim [ ] Nao
- Relatorio resumo correto: [ ] Sim [ ] Nao
- Check final (`manage.py check`): [ ] Sim [ ] Nao

## 8. Comando final de saude

```powershell
python manage.py check
```

Se retornar `System check identified no issues`, backend validado.
