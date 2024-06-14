import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# cofig file
import yaml

import time

from random import *

class Config():
    
    def loadConfig(self):
        with open("config.yaml", 'r') as file:
            config = yaml.safe_load(file)
        return config

class GcpConnect(Config):
    
    def __init__(self):
        self.config = self.loadConfig()
    
    def authorize(self):
        
        # Autoryzacja z użyciem danych uwierzytelniających
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.config['GcpConnect']['credentials_file'], self.config['GcpConnect']['scope'])
        return gspread.authorize(credentials) # return client

class Xlsx(Config):
    
    def __init__(self, gClient):
        
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
    
    
class Game(Config):
    
    def __init__(self):
        self.config = self.loadConfig()
        
    def dictionaryGame(self, dictionary):
        idx = self.config[user][0]
        if user in self.config['Users']:
            sizeDict = len(dictionary)
            while(loop):
                sRow = randrange(sizeDict)
                if dictionary[sRow][idx]:
                    print(dictionary[sRow][idx])
                    time.sleep(self.config['dictionaryBreak'])
                    if dictionary[sRow][idx+1:idx+3][0]:
                        print(dictionary[sRow][idx+1:idx+3][0])
                    elif dictionary[sRow][idx+1:idx+3][1]:
                        print(dictionary[sRow][idx+1:idx+3][1])
                    elif dictionary[sRow][idx+1:idx+3][0] == '':
                        print('You need to translate on your own :).')
                        continue
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
    
    val = int(input(f"Wybierz: \n1) Słownik - losuje słowko, po {config['dictionaryBreak']} s. wyswietla sie tłumaczenie\n2) Uzupelnienie zdan\nPodaj cyfre: "))
    
    if val == 1:
        # DICTIONARY
        sheet2 = xlsx.openSheet(2) # get the second worksheet
        df2 = xlsx.getAll(sheet2)
        
        Game().dictionaryGame(df2[1:])  # only dictionary words    
    elif val == 2:
        print('Game is not ready.')  
    else:
        break
