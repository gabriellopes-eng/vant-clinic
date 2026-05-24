# Instruções para o GitHub Copilot — Projeto VANT

Este repositório contém o backend do sistema VANT, um sistema web para gestão de clínicas de estética.

## Tecnologias obrigatórias

- Python
- Django
- SQLite
- Git/GitHub

## Objetivo

Implementar primeiro todo o backend do sistema.

O front-end será feito depois por Guilherme. Portanto, neste momento, não criar layout avançado, CSS complexo ou JavaScript.

## Apps Django desejados

- core
- clientes
- profissionais
- servicos
- agendamentos
- pagamentos
- relatorios

## Padrão de código

- Usar código simples.
- Usar nomes em português.
- Separar responsabilidades por apps.
- Usar models.py, forms.py, views.py, urls.py e admin.py.
- Criar templates mínimos apenas para testar rotas.
- Não usar Django REST Framework agora.
- Não criar microsserviços.

## Regra principal

O sistema não pode permitir dois agendamentos no mesmo horário para o mesmo profissional.

Essa validação deve ficar no backend.