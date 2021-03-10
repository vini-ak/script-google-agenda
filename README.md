# Script Google Agenda 

### 🐍 A ideia deste projeto é criar um script em Python que automatiza o uso da API do Google Agenda.
==============================

Tabela de Conteúdos

==============================

<!--ts-->
   * [Sobre](#Sobre)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Instalação](#instalacao)
   * [Como usar](#como-usar)
      * [Pre Requisitos](#pre-requisitos)
      * [Local files](#local-files)
      * [Remote files](#remote-files)
      * [Multiple files](#multiple-files)
      * [Combo](#combo)
   * [Tecnologias](#tecnologias)
<!--te-->
#### Status do Projeto: Em construção... 🏭

### Features

- [x] Listar próximos eventos
- [x] Criar um evento e convidar pessoas da organização
- [ ] Adicionar os funcionários da Seed ao evento sem precisar digitar o email completo
- [ ] Melhorar a forma de passar a data de início e tempo de duração na criação do evento
- [ ] Criar uma flag para cada projeto atual
- [ ] Cancelar um evento
- [ ] Atualizar um evento


### Pré-requisitos

Antes de começar, você precisa ter o [Python](https://www.python.org/downloads/) na versão 3.x instalado na sua máquina. Também é recomendado que você tenha uma certa noção de como utilizar linha de comando.

Você precisará também ter um arquivo credentials.json que armazene os valores da sua credencial para a API do [Google Calendar](https://developers.google.com/calendar/quickstart/python). 


### 🍳 Preparando o ambiente

```bash
# Criando o amvbiente virtual
$ python3 -m venv google_agenda

# Copie todos os arquivos para dentro da virtual env
$ mv * google_agenda/

# Vá para a pasta google_agenda
$ cd google_agenda/

# Instale as dependências
$ source bin/activate

# Instalando as dependências
$ pip install -r requirements.txt

```


### ⚠️ Observação

Devido ao dataset utilizado para esta versão do script ser um objeto interno da Seed a Bit Tecnologia, eu decidi não dispor publicamente o arquivo juntamente com o restante do código.

Isso significa que o código não conseguirá recuperar os emails dos membros da empresa e que não será possível criar eventos utilizando as tags --all, --comercial, --executiva, --gp, --markerting e --projetos.

Caso queira, pode utilizar o script normalmente e inserir o email dos usuários um a um, ou pode entrar em contato comigo para que eu possa enviar o arquivo csv para você, ok? 😉


### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/downloads/)
- [Google Calendar API](https://developers.google.com/calendar/quickstart/python)
- [Pandas](https://pandas.pydata.org/)
