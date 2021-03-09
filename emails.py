import pandas as pd

class EmailsMembros:
    def __init__(self):
        self._membros = pd.read_csv('seed_2021_1.csv')
    
    @property
    def membros(self):
        return self._membros

    def getAllEmails(self):
        ''' Retorna o email de todos os membres. '''
        allEmails = self.membros
        return allEmails
    
    def getEmails(self, area = None):
        if area is None:
            return self.getAllEmails()
        else:
            return self.membros[self.membros['ÁREA'] == area.upper()]["E-MAIL"]
