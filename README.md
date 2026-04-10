# 🗳️ Sistema de Votação Digital  
### Projeto Integrador I – Engenharia de Software  

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Database](https://img.shields.io/badge/database-MySQL-orange)
![License](https://img.shields.io/badge/license-acadêmico-lightgrey)

---

## 📌 1. Sobre o Projeto  
Este projeto consiste no desenvolvimento do **backend de um sistema de votação digital fictício**, com finalidade exclusivamente acadêmica, no contexto da disciplina de Projeto Integrador I.

A proposta tem como objetivo integrar conhecimentos fundamentais das áreas de:
- Programação em Python  
- Banco de Dados Relacional (MySQL)  
- Segurança da Informação  
- Álgebra Linear aplicada à criptografia  

O sistema opera via **linha de comando (CLI)**, priorizando o raciocínio lógico, a organização modular do código e a manipulação estruturada de dados.

---

## 🎯 2. Objetivos  
- Desenvolver um sistema funcional de votação digital  
- Garantir a integridade e consistência dos dados  
- Implementar validações matemáticas (CPF e Título de Eleitor)  
- Aplicar criptografia utilizando Cifra de Hill  
- Registrar eventos críticos por meio de logs  
- Gerar relatórios confiáveis de apuração  

---

## 👥 3. Integrantes do Grupo  

- AMANDA DE SOUSA TOMAZ
- HENRIQUE KENJI TUTIYA
- JÚLIA ANDRADE GUARNIERI
- LARISSA SOUZA QUITO SAMPAIO
- PEDRO HENRIQUE SANCHES AGATTI GODOY
- THOMAS KRAUSE ARENA
---

## 🛠️ 4. Tecnologias Utilizadas  
| Tecnologia | Descrição |
|-----------|----------|
| Python 3.x | Linguagem principal do sistema |
| MySQL | Banco de dados relacional |
| mysql.connector | Conexão Python ↔ MySQL |
| datetime | Manipulação de data e hora |
| random | Geração de dados aleatórios |
| time | Controle de execução |
| Git/GitHub | Versionamento e colaboração |

---

## ⚙️ 5. Funcionalidades  

### 🔧 5.1 Módulo de Gerenciamento  
- Cadastro de eleitores  
- Validação de CPF e título de eleitor  
- Geração de chave de acesso  
- Edição e remoção de registros  
- Listagem e busca de dados  
- Gerenciamento de candidatos (opcional)  

---

### 🗳️ 5.2 Módulo de Votação  
- Abertura da votação (apenas mesário)  
- Execução da zerézima  
- Identificação do eleitor  
- Registro de votos  
- Bloqueio de voto duplicado  
- Encerramento seguro da votação  

---

### 📊 5.3 Resultados  
- Boletim de urna  
- Identificação do vencedor  
- Estatísticas de comparecimento  
- Votos por partido  
- Validação de integridade  

---

### 🔍 5.4 Auditoria  
- Registro de logs de ocorrências  
- Monitoramento de acessos  
- Registro de tentativas inválidas  
- Exibição de protocolos de votação  

---

## 🔐 6. Segurança da Informação  
O sistema implementa criptografia utilizando a **Cifra de Hill**, aplicada aos seguintes dados:
- CPF  
- Chave de acesso  
- Protocolo de votação  

Essa abordagem garante:
- Sigilo das informações  
- Integridade dos dados  
- Proteção contra acessos indevidos  

> ⚠️ Observação: A Cifra de Hill é utilizada exclusivamente para fins didáticos.

---

## ▶️ 7. Como Executar o Projeto  

### 7.1 Clonar o repositório  
```bash
git clone https://github.com/PedroSanchesAgatti/ProjetoIntegrador01.git


