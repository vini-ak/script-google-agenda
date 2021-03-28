'''
As credenciais foram criadas com a conta vinicius.vieira@seedabit.org.br.
Lembrar de alterar para as credenciais da conta projetos@seedabit.org.br

TODO: Não esquecer de remover as credenciais quando for subir o projeto para o Github!!!

Criar a chave da API da Google Calendar: https://developers.google.com/calendar/quickstart/python
'''

from __future__ import print_function
import pickle
import os.path
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from modules.emails import EmailsMembros
from modules.calendar import Calendar
from modules.format_time import DateTimeFormater


class GoogleAgenda:
    ''' Classe responsável pela integração com as credenciais do Google Agenda. '''
    def __init__(self, credentials = None):
        self.__credentials = credentials
        self._scopes = ['https://www.googleapis.com/auth/calendar']
    
    @property
    def credentials(self):
        return self.__credentials
    
    @credentials.setter
    def credentials(self, value):
        self.__credentials = value
    
    def getTokenPickle(self):
        ''' Recuperar o arquivo token de acesso e refresh do usuário.'''
        try:
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    self.credentials = pickle.load(token)
                    return self.credentials
        except:
            print("Arquivo token.pickle inexistente.")
            return None
    
    def login(self):
        self.credentials.refresh(Request())
    
    def getCredentialsJsonData(self):
        flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self._scopes)
        creds = flow.run_local_server(port=0)
        self.credentials = creds
    
    def validatingCredentials(self):
        credenciatials = self.getTokenPickle()

        if not credenciatials or not credenciatials.valid:
            if credenciatials and credenciatials.expired and credenciatials.refresh_token:
                print('As credenciais expiraram. É necessário fazer login!')
                self.login()
            else:
                print('Recuperando as credenciais de credentials.json...')
                self.getCredentialsJsonData()
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.credentials, token)
    
    def showNextEvents(self, number_of_events):
        self.validatingCredentials()
        
        agenda = Calendar(self.credentials)
        agenda.showEvents(number_of_events)
    
    def createEvent(self):
        self.validatingCredentials()
        print("=========================\n")
        print("      CRIAR EVENTO      ")
        print("\n=========================\n")
        titulo = input("Informe um título para o evento: ")
        
        date_time_formater = DateTimeFormater()
        startInBR = input("Horário do evento: ")
        # Formatando o início para ficar em um formato aceito
        startInUTC = date_time_formater.parse(startInBR)
        start = startInUTC.replace(" ", "T") + ":00-03:00" 

        endInBR = input("Término do evento: ")
        # Formatando o fim para ficar em um formato aceito
        endInUTC =  date_time_formater.parse(endInBR)
        end = endInUTC.replace(" ", "T") + ":00-03:00" 

        emailMembros = EmailsMembros()

        if len(sys.argv) < 3:
            emails = input("Insira os emails a serem convidados: ")
            emails = emails.split(" ")
        else:
            area = sys.argv[2][2:]
            isArea = area in ['projetos', 'executiva', 'comercial', 'marketing', 'adm-fin', 'gp']

            if isArea:
                emails = emailMembros.getEmails(area)
            elif area == "negocios":
                emailsComercial = emailMembros.getEmails('comercial')   # Recuperando os emails de marketing
                emailsMarketing = emailMembros.getEmails('marketing')   # Recuperando os emails de comercial
                emails = emailsComercial.append(emailsMarketing)        # Gerando uma lista com email de ambas

            elif area == "all":
                emails = emailMembros.getAllEmails()
            elif area == "projeto-pupylex":
                emails = ["vinicius.vieira@seedabit.org.br", "isadora.tavares@seedabit.org.br", "vinicius.cirne@seedabit.org.br", "manussa.raphaela@seedabit.org.br", "igor.macedo@seedabit.org.br", "rafaella.jordao@seedabit.org.br"]
            else:
                raise Exception("Não foi possível recuperar os emails da área. Tag passada (%s) não é uma área da Seed." % sys.argv)

        
        print("\n=========================\n")
        print("Convocando a lista de emails: \n")
        for email in emails:
            print(email)
        print("\n=========================\n")
        
        agenda = Calendar(self.credentials)
        agenda.createEvent(titulo, start=start, end=end, emails=emails)

        




def main():
    ''' Retornando os próximos eventos. '''

    googleAgenda = GoogleAgenda()

    if len(sys.argv) < 2:
        print(sys.argv)
        raise Exception("Número de parâmetros insuficiente")

    # Recuperando a flag passada junto com o comando
    arg = sys.argv[1]

    if arg == '--show' or arg == '-s':
        googleAgenda.showNextEvents(10)
    elif arg == '--new' or arg == '-n':
        googleAgenda.createEvent()
        
    else:
        # TODO: Criar um parâmetro --help
        raise Exception("Parâmetro inválido.")

        
if __name__ == '__main__':
    main()