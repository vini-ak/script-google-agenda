import datetime
from googleapiclient.discovery import build
from modules.event import Event


class Calendar:
    ''' Classe responsável por fazer a integração com a chamada da API. '''
    def __init__(self, credenciatials):
        self._service = build('calendar', 'v3', credentials=credenciatials)

    @property
    def service(self):
        return self._service

    
    def getEventsFromCalendar(self, number_of_events):
        ''' Função que recupera os eventos do calendário. '''
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Retornando os %d próximos eventos' % (number_of_events))

        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=number_of_events, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events


    def showEvents(self, number_of_events):
        ''' Função que mostra os eventos na tela do usuário. '''
        events = self.getEventsFromCalendar(number_of_events)

        if not events:
            print('Sua agenda está completamente vazia.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])


    def createEvent(self, titulo, start = "", end = "", emails = [], description = "", location = None):
        '''
        Método responsável por criar um evento.
        TODO: Implementar a passagem de parâmetros para poder criar os eventos reais.
        '''

        attendees = list(map(lambda x: {'email': x}, emails)) # Emails a serem convidados

        event = Event(titulo, location, description, start, end, attendees) 

        event = self.service.events().insert(calendarId='primary', body=event.body).execute()
        print('Evento criado com sucesso! Segue o link para vê-lo no seu Google Agenda: %s' % (event.get('htmlLink')))
