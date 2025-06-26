# Projeto Leitor de HQs Power Rangers

<p align="center">
    <img src="./static/assets/logo.png" alt="Logo do Projeto" width="250"/>
</p>

## Sobre o Projeto

Este projeto tem como objetivo criar uma plataforma web para leitura das HQs dos **Power Rangers**, armazenadas no Mega Drive do desenvolvedor. A proposta é fornecer uma experiência intuitiva e segura para leitura, com autenticação de usuários e controle de acesso baseado em permissões personalizadas.

## Funcionalidades

* 🔑 **Login com autenticação de usuários**
* 📋 **Controle de permissões por tipo de usuário**
* 🗃️ **Acesso seguro às pastas de HQs hospedadas no Mega**
* 👁️ **Interface web responsiva para leitura online das HQs**
* 🔍 **Organização por série, edição e tipo de acesso**

## Tecnologias Utilizadas

* **Python** (3.x)
* **Flask** - framework web para backend
* **Jinja2** - renderização de templates HTML
* **Mega.py** - biblioteca de integração com o armazenamento na nuvem Mega
* **HTML/CSS/JavaScript** - interface do usuário

## Estrutura de Permissões

* **Administrador**: acesso total a todas as pastas e gestão de usuários
* **Usuário Premium**: acesso às séries completas e lançamentos
* **Usuário Comum**: acesso limitado a edições básicas

## Como Funciona a Integração com o Mega

A biblioteca `mega.py` é utilizada para:

* Autenticar com a conta do Mega
* Listar os arquivos e pastas de HQs disponíveis
* Gerar links temporários para leitura online (com opção de download, caso necessário)

## Objetivo Final

O sistema foi pensado para criar um **ambiente ideal de leitura** das HQs dos Power Rangers, facilitando o acesso à coleção digital, com organização e segurança.

## Instalação e Execução

### Clonar o repositório

```bash
git clone https://github.com/seuusuario/projeto-hqs-power-rangers.git
cd projeto-hqs-power-rangers
```

### Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou no Windows
env\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o projeto

```bash
python main.py
```

## Estrutura Inicial do Projeto

```
projeto-hqs-power-rangers/
├── app/
│   ├── templates/
│   ├── static/
│   ├── routes.py
│   ├── auth.py
│   └── mega_integration.py
├── main.py
├── requirements.txt
└── README.md
```

## Licença

Este projeto é de uso pessoal. Não é permitida a distribuição ou comercialização das HQs.

---

Desenvolvido com ❤️ para organização e apreciação pessoal das HQs Power Rangers.
