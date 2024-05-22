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


gcp = GcpConnect()
client = gcp.authorize()
sheet = client.open(gcp.sheet_name).sheet1

# get all
data = sheet.get_all_values()

#print(data)

column_names = ['week','data','Beata','tłumaczenie','t1','Marta','tłumaczenie','t2']

df = pd.DataFrame(data, columns=column_names)


print(df)