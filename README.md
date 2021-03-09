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