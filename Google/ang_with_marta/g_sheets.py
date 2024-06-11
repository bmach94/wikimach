import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

class GcpConnect:
    
    sheet_name = 'Gra w słówka'
    # Ścieżka do pliku JSON z kluczami dostępu
    credentials_file = 'secrets/angwithmarta.json'

    # Zakres uprawnień
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    def authorize(self):
        # Autoryzacja z użyciem danych uwierzytelniających
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)
        return gspread.authorize(credentials) # return client

class Xlsx:
    
    sheet_name = 'Gra w słówka'
    
    def __init__(self, gClient, columnNames = ['week','data','Beata','tłumaczenie','t1','Marta','tłumaczenie','t2']):
        self._columnNames = columnNames
        self.gclient = gClient
        
    # connect with sheet    
    def openSheet(self):
        return self.gclient.open(self.sheet_name).sheet1
        
    # get all values    
    def getAll(self, sheet):
        #sheet = xlsx.openSheet()
        return sheet.get_all_values()
    
    # read all columns
    def pd_returnAll(self):
        return pd.DataFrame(self.getAll(self.openSheet()), columns=self._columnNames)
    
# connect with GCP    
gcp = GcpConnect()
client = gcp.authorize()

# connect with sheet
xlsx = Xlsx(client)
# print all columns
print(xlsx.pd_returnAll())