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
    def openSheet(self, sheetNumber=1):
        if sheetNumber == 2:
            return self.gclient.open(self.sheet_name).get_worksheet(1) # the second worksheet
        return self.gclient.open(self.sheet_name).sheet1
        
    # get all values    
    def getAll(self, sheet):
        #sheet = xlsx.openSheet()
        return sheet.get_all_values()
    
    # read all columns, return dataframe
    def pd_returnAll(self):
        data = self.getAll(self.openSheet())
        return pd.DataFrame(data)
    
# connect with GCP    
gcp = GcpConnect()
client = gcp.authorize()

# connect with sheet
xlsx = Xlsx(client)
# print all columns
#print(xlsx.pd_returnAll())

#df = xlsx.pd_returnAll()
#print(df[2]) # #english

sheet2 = xlsx.openSheet(2) # get the second worksheet
df2 = xlsx.getAll(sheet2)
#print(df2[2])

user = "Marta"

dictionary = df2[1:]
if user == "Beata":
    for i in dictionary: # print all
        print(i[0:3]) # [1:] - all; [0] - row; [] - columns
elif user == "Marta":
    for i in dictionary: # print all
        print(i[4:7]) # [1:] - all; [0] - row; [] - columns