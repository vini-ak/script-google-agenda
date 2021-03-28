import datetime

class DateTimeFormater:
    
    def agora(self):
        return datetime.datetime.utcnow().isoformat()

    def parseData(self, data):
        dia, mes, ano = data.split('/')
        return ano+"-"+mes+"-"+dia

    def parse(self, data_hora):
        data, hora = data_hora.split(" ")
        dataParsed = self.parseData(data)
        return dataParsed + " " + hora


class TimeCalculator:
    def __init__(self, data_inicio):
        self._data_inicio = datetime.datetime.strptime(data_inicio
    , "%d/%m/%Y %H:%M")

    def add(self, minutes):
        time_change = datetime.timedelta(minutes=minutes)
        result = self._data_inicio + time_change
        return str(result)
        