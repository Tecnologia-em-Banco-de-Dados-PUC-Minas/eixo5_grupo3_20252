# PREVISÃO DE INADIMPLÊNCIA DE CRÉDITO: ARQUITETURA DE DADOS EM NUVEM

**Projeto do Eixo 5 - Tecnologia em Banco de Dados 2025/2**

**Integrantes:** Rodrigo Borges Martins, Douglas Pereira Martins, Lucas Cardoso Mendonça, Lucas Gomes de Oliveira e Luan Lacerda Ramos

---

## ETAPA 1: INÍCIO DO PROJETO

### Resumo

Este projeto foca no desenvolvimento de um modelo supervisionado de aprendizado de máquina para prever a inadimplência na concessão de crédito. O objetivo principal é extrair padrões discriminativos que permitam antecipar o risco de crédito, fornecendo suporte a decisões financeiras e auxiliando na minimização de perdas e otimização dos protocolos de aprovação de crédito.

As vantagens esperadas incluem:
- Redução de perdas financeiras
- Agilidade na tomada de decisão
- Personalização das condições de crédito de acordo com o perfil de risco do cliente
- Garantia de maior eficiência operacional

Adicionalmente, a aplicação de técnicas de aprendizado de máquina proporcionará análises mais precisas e escaláveis, contribuindo para a sustentabilidade e competitividade das instituições financeiras no mercado.

---

### 1.1 Problema

A inadimplência na concessão de crédito representa um desafio significativo para as empresas, impactando diretamente sua saúde financeira, operações e capacidade de crescimento.

#### Problemas Financeiros
- **Redução do fluxo de caixa:** A falta de recebimento compromete o capital de giro, essencial para cobrir despesas operacionais, pagamentos a fornecedores e salários
- **Aumento dos custos operacionais:** Há necessidade de destinar recursos para provisões de perdas e investir em processos de cobrança, sejam eles jurídicos ou administrativos
- **Perda de lucratividade:** Os atrasos nos pagamentos reduzem as margens de lucro projetadas, afetando a rentabilidade geral da empresa

#### Problemas Operacionais
- **Paralisação de investimentos:** Recursos que seriam alocados em expansão, inovação ou melhorias são comprometidos pela necessidade de cobrir dívidas
- **Maior tempo e esforço em cobrança:** Equipes são desviadas de suas funções primárias para focar em renegociações e recuperação de dívidas, gerando ineficiência
- **Risco de desequilíbrio na cadeia de suprimentos:** A dificuldade em honrar pagamentos pode gerar tensões e comprometer o relacionamento com fornecedores e parceiros, afetando a continuidade operacional

Além disso, a inadimplência acarreta problemas estratégicos e jurídicos, corroendo a liquidez e dificultando o crescimento sustentável. Consequentemente, as empresas são compelidas a intensificar seus investimentos em análise de crédito, diversificação de clientes e no desenvolvimento de políticas de cobrança mais eficazes.

---

### 1.2 Contexto

Para a análise preditiva, será utilizado o **Credit Risk Dataset** disponível no Kaggle:
- **Link:** https://www.kaggle.com/datasets/laotse/credit-risk-dataset

A escolha deste dataset se justifica pelo seu volume e variabilidade, que o tornam representativo do cenário de uma empresa real. Isso permitirá explorar diferentes situações relacionadas à concessão de crédito e ao risco de inadimplência, facilitando a análise e a estruturação de um modelo de machine learning robusto e com alto potencial de aplicação prática no ambiente empresarial.

---

## 2. Objetivos

### Objetivo Geral
Desenvolver um algoritmo de classificação baseado em aprendizado supervisionado capaz de prever a probabilidade de um cliente se tornar inadimplente ou atrasar pagamentos, utilizando dados históricos como base para a análise.

### Objetivos Específicos
- **Redução de riscos financeiros:** Identificar precocemente clientes com alto risco de inadimplência, permitindo ações preventivas
- **Agilização de processos decisórios:** Fornecer uma ferramenta que otimize o processo de aprovação de crédito, tornando-o mais rápido e assertivo
- **Personalização de condições de crédito:** Possibilitar a oferta de condições de crédito adaptadas ao perfil de risco de cada cliente
- **Implementação de uma arquitetura tecnológica robusta:** Desenvolver um sistema que suporte a análise preditiva de crédito de forma eficiente e escalável

A meta final é transformar a gestão de risco de crédito de um modelo reativo para um modelo proativo e preditivo, promovendo maior eficiência operacional e rentabilidade para as instituições.

---

## ETAPA 2: COLETA DE DADOS

## 3. Planejamento de Governança e Modelo de Dados

A coleta de dados constitui fase fundamental para o sucesso de projetos de banco de dados e machine learning. Nesta etapa foram definidas estratégias para extração, armazenamento e gerenciamento dos dados utilizados no projeto. A coleta será realizada a partir da base disponível no Kaggle, porém foram implementadas decisões importantes sobre infraestrutura, pipeline de dados e governança para simular ambiente corporativo real.

### 3.1 Estratégia de Governança de Dados

Foi elaborada estratégia de governança que define requisitos, procedimentos, funções e responsabilidades para todo o ciclo de vida dos dados. A estrutura de gerenciamento estabelece:
- Controles de qualidade, segurança e rastreabilidade
- Definição de papéis e responsabilidades
- Políticas de acesso e uso dos dados
- Procedimentos de backup e recuperação
- Mecanismos de auditoria e monitoramento contínuo

### 3.2 Modelo de Dados e Armazenamento

Os dados serão armazenados no formato **Parquet** devido a duas características principais:
- **Baixo custo de consumo:** Estrutura colunar que otimiza armazenamento e reduz custos de consulta em ambientes de nuvem
- **Alta performance:** Leitura mais rápida e eficiente, ideal para processamento paralelo

Ao final do processo de ETL, os dados estarão limpos e estruturados, prontos para consumo pelos modelos de machine learning.

### 3.3 Infraestrutura e Pipeline de Dados

A implementação da infraestrutura será realizada na **Amazon Web Services (AWS)** utilizando serviços especializados para construção de pipeline robusto e escalável. A arquitetura foi projetada considerando aspectos de performance, custo e facilidade de manutenção, seguindo boas práticas de engenharia de dados.

### 3.4 Arquitetura de Armazenamento e Processamento

- **AWS S3 (Simple Storage Service):** Armazenamento de arquivos no formato Parquet, proporcionando durabilidade e escalabilidade
- **AWS Glue:** Pipeline de ETL totalmente gerenciado que simplifica preparação e carregamento de dados
- **AWS Athena:** Consultas aos dados através de SQL padrão sem necessidade de infraestrutura adicional

### 3.5 Infraestrutura como Código e Controle de Versão

Para garantir replicabilidade e padronização do ambiente, a infraestrutura será criada utilizando **Infraestrutura como Código (IaC)**. Os scripts estarão disponibilizados no repositório Git do projeto, permitindo que membros da equipe repliquem a estrutura em suas próprias contas AWS.

Todo código-fonte do pipeline de ETL e scripts de IaC serão versionados através de sistema de controle de versão com implementação de fork do repositório principal para desenvolvimento e posterior integração via pull request.

### 3.6 Controle e Rastreabilidade

O projeto implementa sistema abrangente de controle e rastreabilidade para garantir qualidade e governança adequada dos dados e processos. A documentação completa será mantida no repositório Git, explicando procedimentos para replicação da infraestrutura e utilização do pipeline de dados.

### 3.7 Sistema de Monitoramento

Foi implementado sistema de TAGs simulando identificadores de tarefas similar a plataformas como JIRA, permitindo:
- Controle granular sobre desenvolvimento
- Práticas de integração contínua e entrega contínua (CI/CD)
- Rastreamento completo de alterações

---

## 4. Documentação e Repositório

A documentação técnica abrange desde configuração inicial da infraestrutura até procedimentos operacionais do pipeline de dados.

**Repositório GitHub:** https://github.com/lucascmendonca/eixo5_grupo3_20252

### Status do Projeto
- ✅ Etapa 1: Concluída
- ✅ Etapa 2: Concluída
- 🔄 Próxima Etapa: 3 - Pré-processamento de dados

### Próxima Etapa
A Etapa 3 contemplará:
- Limpeza, transformação e junção dos dados
- Registro das ações realizadas
- Compartilhamento dos dados pré-processados
- Atualização do modelo de dados (caso necessário)

Este documento será continuamente atualizado conforme progresso das atividades nas etapas subsequentes do projeto.

---

## 5. Referências

1. Confederação Nacional de Dirigentes Lojistas (CNDL) e Serviço de Proteção ao Crédito (SPC Brasil). **Indicadores de inadimplência no Brasil.** 2024. Disponível em: https://www.cndl.org.br. Acesso em: set. 2025.

2. Kaggle. **Credit Risk Dataset.** Disponível em: https://www.kaggle.com/datasets/laotse/credit-risk-dataset. Acesso em: set. 2025.

3. IBM. **Machine Learning: conceito e aplicação prática.** IBM Knowledge Center, 2024. Disponível em: https://www.ibm.com/think/topics/machine-learning. Acesso em: set. 2025.

4. Amazon Web Services (AWS). **Armazenamento e processamento de dados na nuvem: S3, Glue e Athena.** AWS Documentation, 2025. Disponível em: https://aws.amazon.com/documentation/. Acesso em: set. 2025.

5. Brasil. **Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais - LGPD).** Diário Oficial da União, 2018.

6. Gartner, Inc. **Best Practices in Data Governance.** Gartner Research Report, 2024.
