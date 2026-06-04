# Planejamento da Arquitetura de Software

## 1. Identificacao do Projeto

| Campo | Descricao |
|---|---|
| Nome do Projeto | VANT |
| Grupo | 3 |
| Integrantes | Guilherme Menezes, Jamile Freitas, Gabriel Lopes e Jose Fernandes |

## 2. Visao Geral do Sistema

### 2.1 Descricao do Problema

A prestacao de servicos esteticos e um setor em constante crescimento e, com isso, surgem tambem desafios relacionados a organizacao e a gestao dos atendimentos. Muitos estabelecimentos da area, como clinicas de estetica, saloes de beleza e profissionais autonomos, ainda utilizam metodos simples para controlar seus servicos, como anotacoes manuais, agendas fisicas ou processos pouco integrados. Embora esses metodos possam funcionar em pequenas rotinas, eles nao oferecem estrutura suficiente para acompanhar o aumento da demanda e a necessidade de maior controle operacional.

Nesse contexto, um dos principais problemas enfrentados e o conflito de agendamentos, que ocorre quando dois atendimentos sao marcados para o mesmo profissional no mesmo horario. Alem disso, a ausencia de um sistema centralizado dificulta o controle de clientes, profissionais, servicos e pagamentos, comprometendo a produtividade da equipe, a qualidade do atendimento e a organizacao do negocio.

Diante desse cenario, o projeto VANT foi desenvolvido como uma solucao voltada para a gestao de clinicas esteticas, com foco na centralizacao das informacoes, na reducao de conflitos de agenda e no apoio a rotina administrativa. O nome VANT representa a proposta do sistema e pode ser compreendido como uma sigla associada a Visao, Agendamento, Negocio e Tratamentos, refletindo a finalidade de oferecer uma visao mais organizada, pratica e eficiente das operacoes da clinica.

### 2.2 Objetivos do Sistema

O intuito do VANT e resolver os problemas relacionados a desorganizacao operacional em clinicas esteticas, por meio da digitalizacao e centralizacao dos principais processos do estabelecimento. O sistema tem como objetivo melhorar a gestao da rotina de atendimentos, reduzir falhas manuais, evitar conflitos de horario e auxiliar no acompanhamento dos servicos realizados e dos pagamentos recebidos.

De forma pratica, o sistema permite o cadastro de clientes, profissionais e servicos esteticos, alem da criacao e do gerenciamento de agendamentos. O VANT tambem possui controle de pagamentos vinculados aos atendimentos e disponibiliza um resumo com indicadores operacionais, contribuindo para uma administracao mais eficiente e segura.

Objetivos especificos:

1. Centralizacao da agenda: permitir que os horarios dos profissionais, os dados dos clientes e os servicos cadastrados sejam organizados em um unico sistema.
2. Prevencao de overbooking: impedir que dois agendamentos ativos sejam realizados no mesmo horario para o mesmo profissional.
3. Organizacao dos atendimentos: possibilitar o cadastro, a edicao, a consulta e o cancelamento de agendamentos de forma estruturada.
4. Controle de pagamentos: permitir o registro do valor, status, data e forma de pagamento dos servicos realizados.
5. Melhoria da eficiencia operacional: reduzir falhas manuais e tornar a rotina administrativa da clinica mais organizada, rapida e confiavel.
6. Apoio a gestao: oferecer uma visao resumida das informacoes da clinica, como total de agendamentos, cancelamentos, servicos cadastrados, pagamentos e valor total recebido.

### 2.3 Publico-Alvo

1. B2B (gestores e profissionais de estetica)
   O sistema e voltado para proprietarios de clinicas de estetica, saloes de beleza, centros de bem-estar e esteticistas autonomos que precisam de uma ferramenta para organizar a rotina de trabalho, controlar horarios, gerenciar clientes, profissionais, servicos e pagamentos, alem de evitar conflitos de agenda.

2. Usuarios operacionais do sistema
   O sistema tambem pode ser utilizado por recepcionistas ou responsaveis pelo atendimento da clinica, que necessitam cadastrar clientes, registrar agendamentos, atualizar informacoes dos servicos, controlar pagamentos e acompanhar a rotina administrativa de forma centralizada.

## 3. Requisitos Arquiteturais

### 3.1 Requisitos Funcionais

| ID | Requisito Funcional |
|---|---|
| RF01 | O sistema deve permitir o cadastro de clientes com nome, telefone, e-mail e informacoes basicas de contato. |
| RF02 | O sistema deve permitir o cadastro de profissionais de estetica, informando nome, especialidade e dados de contato. |
| RF03 | O sistema deve permitir o cadastro dos servicos oferecidos pelo estabelecimento, incluindo nome, descricao, duracao e valor. |
| RF04 | O sistema deve permitir a realizacao de agendamentos vinculando cliente, profissional, servico, data e horario. |
| RF05 | O sistema deve impedir que dois agendamentos sejam registrados no mesmo horario para o mesmo profissional, desde que estejam ativos. |
| RF06 | O sistema deve permitir a consulta dos agendamentos cadastrados no sistema. |
| RF07 | O sistema deve permitir a edicao ou o reagendamento de um atendimento ja marcado. |
| RF08 | O sistema deve permitir o cancelamento de agendamentos. |
| RF09 | O sistema deve permitir o registro do status do pagamento como pendente ou pago. |
| RF010 | O sistema deve permitir que o administrador visualize relatorios simples de agendamentos, cancelamentos, servicos cadastrados e pagamentos. |
| RF011 | O sistema deve permitir o cadastro e a autenticacao de usuarios por meio de login e senha. |

### 3.2 Requisitos Nao Funcionais

| ID | Requisito Nao Funcional |
|---|---|
| RNF01 | O sistema deve ser desenvolvido utilizando a linguagem Python e o framework Django. |
| RNF02 | O sistema deve utilizar banco de dados relacional, inicialmente SQLite, por ser simples e adequado ao desenvolvimento academico. |
| RNF03 | O sistema deve possuir controle de acesso por login e senha para proteger as funcionalidades administrativas. |
| RNF04 | O sistema deve possuir interface web simples, organizada e de facil utilizacao. |
| RNF05 | O codigo-fonte do sistema deve ser versionado e armazenado no GitHub. |

## 4. Restricoes do Projeto

O projeto possui restricoes tecnicas, financeiras e organizacionais.

Como restricao tecnica, o sistema sera desenvolvido em Python utilizando o framework Django. O banco de dados inicial sera SQLite, pois e uma solucao simples, gratuita e suficiente para o desenvolvimento e apresentacao do projeto.

Como restricao financeira, o sistema devera utilizar tecnologias gratuitas e de codigo aberto, evitando custos com licencas, servidores pagos ou ferramentas proprietarias.

Como restricao organizacional, o projeto sera desenvolvido por uma equipe pequena e dentro do prazo definido pela disciplina. Por isso, o escopo sera limitado as funcionalidades principais: cadastro de clientes, cadastro de profissionais, cadastro de servicos, agendamentos, controle de pagamento e relatorios simples.

A hospedagem ainda nao esta definida, podendo ser escolhida posteriormente entre opcoes como Render, Railway, PythonAnywhere ou outro servico compativel com aplicacoes Django.

## 5. Decisoes Arquiteturais

### 5.1 Estilo Arquitetural Escolhido

O estilo arquitetural escolhido para o sistema VANT sera a Arquitetura MVC.

No contexto do Django, o framework utiliza uma variacao chamada MVT, composta por Model, View e Template. Porem, para fins de planejamento arquitetural, essa estrutura pode ser explicada com base na arquitetura MVC.

No sistema VANT, o Model sera responsavel pelos dados e regras ligadas ao banco de dados, a View sera responsavel por controlar as requisicoes e os Templates representarao a interface visual apresentada ao usuario.

### 5.2 Justificativa da Escolha

A arquitetura MVC foi escolhida porque organiza o sistema em partes bem definidas, separando dados, regras de controle e interface do usuario.

Essa separacao facilita o desenvolvimento, a manutencao e a apresentacao do projeto, pois cada parte possui uma responsabilidade clara.

Alem disso, o Django ja oferece uma estrutura pronta que favorece esse tipo de organizacao, permitindo criar models, views, templates, rotas e formularios de forma padronizada.

Para o sistema VANT, a arquitetura MVC e adequada porque o projeto possui funcionalidades diretas, como cadastro de clientes, cadastro de profissionais, cadastro de servicos, agendamento, controle de pagamento e consulta de agendamentos.

Portanto, nao ha necessidade de utilizar uma arquitetura mais complexa, como microsservicos ou arquitetura orientada a eventos.

## 6. Componentes / Servicos

### 6.1 Componentes do Sistema

| ID | Componente | Responsabilidade |
|---|---|---|
| C01 | Componente de Usuarios e Autenticacao | Gerenciar o registro de usuarios, login, logout e a protecao de acesso as funcionalidades do sistema. |
| C02 | Componente de Clientes | Gerenciar o cadastro, consulta, atualizacao e remocao dos clientes da clinica. |
| C03 | Componente de Profissionais | Gerenciar o cadastro dos profissionais, suas especialidades, dados de contato e status de atividade. |
| C04 | Componente de Servicos Esteticos | Gerenciar os servicos oferecidos pela clinica, incluindo descricao, duracao, valor e status. |
| C05 | Componente de Agendamentos | Gerenciar a criacao, consulta, alteracao e cancelamento de agendamentos, alem da validacao de conflitos de horario. |
| C06 | Componente de Pagamentos | Gerenciar os pagamentos vinculados aos agendamentos, incluindo valor, status, data e forma de pagamento. |
| C07 | Componente de Relatorios | Gerenciar a visualizacao de informacoes resumidas sobre agendamentos, cancelamentos, servicos e pagamentos do sistema. |

### 6.2 Servicos do Sistema

| Servico | ID Componente | Descricao |
|---|---|---|
| S01 | C01 | Servico de registro de usuario, responsavel por permitir a criacao de novas contas no sistema. |
| S02 | C01 | Servico de login, responsavel por autenticar o usuario e liberar o acesso as funcionalidades protegidas. |
| S03 | C01 | Servico de logout, responsavel por encerrar a sessao do usuario no sistema. |
| S04 | C01 | Servico de protecao de rotas, responsavel por restringir o acesso aos modulos apenas para usuarios autenticados. |
| S05 | C01 | Servico de redirecionamento de autenticacao, responsavel por encaminhar usuarios nao autenticados para a tela de login. |
| S06 | C02 | Servico de cadastro de clientes, responsavel por registrar nome, telefone, e-mail, observacoes e status do cliente. |
| S07 | C02 | Servico de listagem de clientes, responsavel por consultar os clientes cadastrados no sistema. |
| S08 | C02 | Servico de edicao de clientes, responsavel por atualizar os dados dos clientes ja cadastrados. |
| S09 | C02 | Servico de exclusao de clientes, responsavel por remover clientes do sistema quando necessario. |
| S10 | C02 | Servico de controle de status do cliente, responsavel por indicar se o cliente esta ativo ou inativo. |
| S11 | C03 | Servico de cadastro de profissionais, responsavel por registrar nome, especialidade, telefone, e-mail e status do profissional. |
| S12 | C03 | Servico de listagem de profissionais, responsavel por consultar os profissionais cadastrados no sistema. |
| S13 | C03 | Servico de edicao de profissionais, responsavel por atualizar os dados dos profissionais ja cadastrados. |
| S14 | C03 | Servico de exclusao de profissionais, responsavel por remover profissionais do sistema quando necessario. |
| S15 | C03 | Servico de controle de status do profissional, responsavel por indicar se o profissional esta ativo ou inativo. |
| S16 | C04 | Servico de cadastro de servicos esteticos, responsavel por registrar os procedimentos oferecidos pela clinica. |
| S17 | C04 | Servico de listagem de servicos esteticos, responsavel por consultar os servicos cadastrados. |
| S18 | C04 | Servico de edicao de servicos esteticos, responsavel por atualizar descricao, duracao e valor dos servicos. |
| S19 | C04 | Servico de exclusao de servicos esteticos, responsavel por remover servicos do sistema quando necessario. |
| S20 | C04 | Servico de controle de status do servico, responsavel por indicar se o procedimento esta ativo ou inativo. |
| S21 | C05 | Servico de cadastro de agendamentos, responsavel por registrar atendimentos vinculando cliente, profissional, servico, data e horario. |
| S22 | C05 | Servico de listagem de agendamentos, responsavel por consultar todos os agendamentos cadastrados no sistema. |
| S23 | C05 | Servico de edicao de agendamentos, responsavel por alterar informacoes de atendimentos ja marcados. |
| S24 | C05 | Servico de cancelamento de agendamentos, responsavel por marcar um atendimento como cancelado. |
| S25 | C05 | Servico de validacao de conflito de horario, responsavel por impedir dois agendamentos ativos no mesmo horario para o mesmo profissional. |
| S26 | C06 | Servico de cadastro de pagamentos, responsavel por registrar pagamentos vinculados a um agendamento. |
| S27 | C06 | Servico de listagem de pagamentos, responsavel por consultar os pagamentos cadastrados no sistema. |
| S28 | C06 | Servico de edicao de pagamentos, responsavel por atualizar valor, status, data e forma de pagamento. |
| S29 | C06 | Servico de exclusao de pagamentos, responsavel por remover pagamentos do sistema quando necessario. |
| S30 | C06 | Servico de controle de status do pagamento, responsavel por identificar se o pagamento esta pendente ou pago. |
| S31 | C07 | Servico de totalizacao de agendamentos, responsavel por exibir a quantidade total de agendamentos registrados. |
| S32 | C07 | Servico de totalizacao de cancelamentos, responsavel por exibir a quantidade total de agendamentos cancelados. |
| S33 | C07 | Servico de totalizacao de servicos cadastrados, responsavel por exibir a quantidade total de servicos disponiveis no sistema. |
| S34 | C07 | Servico de totalizacao de pagamentos, responsavel por exibir a quantidade total de pagamentos registrados. |
| S35 | C07 | Servico de calculo do valor total pago, responsavel por somar os pagamentos com status pago e apresentar o resultado no relatorio. |

## 7. Tecnologias Utilizadas

| Categoria | Tecnologia |
|---|---|
| Front-end | HTML, CSS, JavaScript e Templates do Django |
| Back-end | Python com Django |
| Banco de Dados | SQLite |
| API interna | Django Views, Django URLs e Django Forms |
| Hospedagem | A definir. Possiveis opcoes: Render, Railway ou PythonAnywhere. |
| Controle de Versao | Git e GitHub |

## 8. Modelagem Arquitetural

### 8.1 Diagrama de Caso de Uso

O diagrama de caso de uso do VANT deve representar os atores operacionais do sistema, como administrador, recepcionista e usuario autenticado, relacionados aos fluxos de autenticacao, cadastros, agendamentos, pagamentos e relatorios.

### 8.2 Descricao arquitetural

#### Arquitetura MVC

A arquitetura escolhida para o sistema VANT sera a Arquitetura MVC, adaptada ao funcionamento do framework Django.

No Django, a estrutura e conhecida como MVT, formada por Model, View e Template. Mesmo assim, ela pode ser relacionada ao MVC, pois separa a aplicacao em dados, controle e interface.

**Qual sera o papel do Model?**

O Model sera responsavel por representar os dados principais do sistema e fazer a comunicacao com o banco de dados.

1. Cliente
2. Profissional
3. ServicoEstetico
4. Agendamento
5. Pagamento
6. Usuario

Esses Models irao armazenar as informacoes necessarias para o funcionamento do sistema, como dados dos clientes, profissionais, servicos, agendamentos, pagamentos e usuarios autenticados.

**Qual sera o papel da View?**

A View sera responsavel por receber as requisicoes dos usuarios, processar as informacoes e retornar uma resposta.

No Django, as views serao utilizadas para controlar acoes como cadastrar cliente, cadastrar profissional, cadastrar servico, criar agendamento, consultar agendamentos, cancelar horario, registrar pagamento e gerar relatorios.

A View tambem sera responsavel por acionar validacoes antes de salvar os dados no banco de dados.

**Qual sera o papel do Controller?**

No sistema VANT, o papel do Controller sera exercido principalmente pelas Views do Django.

O Controller sera responsavel por controlar o fluxo da aplicacao, recebendo uma acao do usuario, chamando os Models necessarios, aplicando as regras de negocio e retornando a tela adequada.

Por exemplo, quando um usuario tenta marcar um horario, o Controller verifica se aquele profissional ja possui um agendamento ativo no mesmo horario. Caso ja exista um agendamento, o sistema impede a marcacao e exibe uma mensagem de erro.

**Como uma acao do usuario percorre o MVC?**

1. O usuario acessa uma tela do sistema, como a tela de agendamento.
2. A interface envia a solicitacao para o sistema.
3. A View recebe a requisicao e identifica a acao desejada.
4. A View consulta ou altera os dados por meio do Model.
5. O Model acessa o banco de dados SQLite.
6. O banco de dados retorna as informacoes solicitadas.
7. A View processa o resultado.
8. O Template exibe a resposta ao usuario.

**Exemplo pratico**

A recepcionista tenta cadastrar um agendamento para uma cliente as 15h com uma profissional especifica. A View recebe essa solicitacao, consulta o Model Agendamento e verifica se ja existe outro atendimento ativo marcado para a mesma profissional nesse horario. Se nao existir conflito, o sistema salva o agendamento. Se existir conflito, o sistema exibe uma mensagem informando que o horario ja esta ocupado.

**Quais dados estarao no Model?**

1. Dados dos clientes: nome, telefone, e-mail e observacoes.
2. Dados dos profissionais: nome, especialidade, telefone, e-mail e status.
3. Dados dos servicos esteticos: nome, descricao, duracao e valor.
4. Dados dos agendamentos: cliente, profissional, servico, data, horario e status.
5. Dados dos pagamentos: forma de pagamento, valor, data e status do pagamento.
6. Dados dos usuarios: login, senha e autenticacao de acesso.

**Quais telas estarao na View?**

1. Tela de login
2. Tela de registro de usuario
3. Tela inicial
4. Tela de cadastro de clientes
5. Tela de cadastro de profissionais
6. Tela de cadastro de servicos esteticos
7. Tela de novo agendamento
8. Tela de listagem de agendamentos
9. Tela de edicao de agendamento
10. Tela de registro de pagamento
11. Tela de relatorios simples

**Quais regras de controle ficarao no Controller?**

1. Impedir dois agendamentos ativos no mesmo horario para o mesmo profissional.
2. Validar se todos os campos obrigatorios foram preenchidos.
3. Permitir acesso ao sistema apenas para usuarios autenticados.
4. Permitir o cancelamento ou a edicao apenas de agendamentos existentes.
5. Atualizar o status do agendamento para agendado, cancelado ou concluido.
6. Atualizar o status do pagamento para pendente ou pago.
