import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# cofig file
import yaml

import time

class Config():
    
    def loadConfig(self):
        with open("config.yaml", 'r') as file:
            config = yaml.safe_load(file)
        return config

class GcpConnect(Config):
    
    def __init__(self):
        self.config = self.loadConfig()
    
    def authorize(self):
        
        #config = self.loadConfig()
        # Autoryzacja z użyciem danych uwierzytelniających
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.config['GcpConnect']['credentials_file'], self.config['GcpConnect']['scope'])
        return gspread.authorize(credentials) # return client

class Xlsx(Config):
    
    def __init__(self, gClient, columnNames = ['week','data','Beata','tłumaczenie','t1','Marta','tłumaczenie','t2']):
        self._columnNames = columnNames
        self.gclient = gClient
        self.config = self.loadConfig()
    # connect with sheet    
    def openSheet(self, sheetNumber=1):
        
        if sheetNumber == 2:
            return self.gclient.open(self.config['Xlsx']['sheet_name']).get_worksheet(1) # the second worksheet
        return self.gclient.open(self.config['Xlsx']['sheet_name']).sheet1
        
    # get all values    
    def getAll(self, sheet):
        #sheet = xlsx.openSheet()
        return sheet.get_all_values()
    
    # read all columns, return dataframe
    def pd_returnAll(self):
        data = self.getAll(self.openSheet())
        return pd.DataFrame(data)
    

# connect with GCP    
client = GcpConnect().authorize()

# connect with sheet
xlsx = Xlsx(client)

# load parameters
config = Config().loadConfig()

loop = True

while (loop):
    print('Wybierz słówka uzytkownika, których chcesz się uczyć: ')
    for u in config['Users']:
        print(f'{u}\n')
    
    user = input()
    
    val = int(input('Wybierz: \n1) Słownik - losuje słowko, po 5 s. wyswietla sie tłumaczenie\n2) Uzupelnienie zdan\nPodaj cyfre: '))
    
    if val == 1:
        # DICTIONARY
        sheet2 = xlsx.openSheet(2) # get the second worksheet
        df2 = xlsx.getAll(sheet2)

        dictionary = df2[1:]
        if user in config['Users']:
            
            for sRow in range(5):
                idx = config[user][0]
                print(dictionary[sRow][idx])
                time.sleep(1)
                print(dictionary[sRow][idx+1:idx+3])
                    
    break
