Você será meu assistente de desenvolvimento backend para o projeto VANT.

Eu sou Gabriel Lopes e serei responsável por implementar todo o backend do projeto. O Guilherme ficará responsável pelo front-end somente depois que o backend estiver pronto.

Portanto, neste momento, o foco é 100% no backend.

Contexto do projeto:
O VANT é um sistema web para clínicas de estética, salões de beleza e profissionais autônomos. O objetivo é organizar agendamentos, evitar conflitos de horário, centralizar clientes, profissionais, serviços, pagamentos e gerar relatórios simples.

Tecnologias obrigatórias:
- Python
- Django
- SQLite
- Git/GitHub

Arquitetura:
O projeto deve seguir uma organização compatível com Django/MVC, sabendo que o Django usa MVT.

Apps desejados:
- core
- clientes
- profissionais
- servicos
- agendamentos
- pagamentos
- relatorios

Funcionalidades mínimas do backend:
1. Autenticação de usuários usando o sistema padrão do Django.
2. Cadastro, listagem, edição e exclusão de clientes.
3. Cadastro, listagem, edição e exclusão de profissionais.
4. Cadastro, listagem, edição e exclusão de serviços estéticos.
5. Criação de agendamentos.
6. Consulta de agendamentos.
7. Reagendamento.
8. Cancelamento de agendamento.
9. Registro de pagamento associado a um agendamento.
10. Relatórios simples com totais de agendamentos, cancelamentos, serviços e pagamentos.

Regra principal:
O sistema não pode permitir dois agendamentos no mesmo horário para o mesmo profissional.

Essa validação deve existir no backend, não apenas na interface.

Regras de implementação:
- Não criar funcionalidades fora do escopo.
- Não implementar front-end avançado agora.
- Não usar JavaScript agora.
- Não usar API REST agora.
- Usar Django padrão com views, forms, urls, models e templates mínimos.
- Usar nomes em português para os models principais.
- Escrever código simples, acadêmico e fácil de explicar na apresentação.
- Priorizar organização e clareza.
- Sempre explicar rapidamente o que foi criado antes de alterar muitos arquivos.
- Quando criar arquivos, indique o caminho completo.
- Quando houver decisão técnica, escolha a solução mais simples para um projeto acadêmico.

Ordem obrigatória:
1. Criar ou revisar a estrutura inicial do projeto Django.
2. Criar os apps: core, clientes, profissionais, servicos, agendamentos, pagamentos e relatorios.
3. Configurar os apps no settings.py.
4. Criar os models: Cliente, Profissional, ServicoEstetico, Agendamento e Pagamento.
5. Registrar os models no admin.py.
6. Criar forms.py para cada app necessário.
7. Criar views CRUD para clientes, profissionais e serviços.
8. Criar views para agendamento.
9. Criar a validação contra conflito de horário.
10. Criar views para pagamentos.
11. Criar views para relatórios simples.
12. Criar urls.py em cada app e conectar tudo ao urls.py principal.
13. Criar templates mínimos apenas para testar as rotas.
14. Criar migrations e orientar os comandos finais.

Agora comece pela Etapa 1.

Me diga exatamente:
1. Quais comandos devo executar no terminal.
2. Qual estrutura de pastas será criada.
3. Quais arquivos serão alterados.
4. O que será feito em cada arquivo.
5. Depois disso, gere o código necessário para iniciar o backend do projeto.