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

