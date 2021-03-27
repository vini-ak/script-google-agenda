class Event:
    def __init__(self, titulo, location, description, start, end, attendees):
        self._body = {
            'summary': titulo,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start,
                'timeZone': 'America/Recife',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'America/Recife',
            },
            # 'recurrence': [
            #     'RRULE:FREQ=DAILY;COUNT=2'
            # ],
            'attendees': attendees,
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    
    @property
    def body(self):
        return self._body
    