import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GcpConnect:
    
    # Ścieżka do pliku JSON z kluczami dostępu
    credentials_file = './angwithmarta.json'

    # Zakres uprawnień
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    def authorize(self):
        # Autoryzacja z użyciem danych uwierzytelniających
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)
        return gspread.authorize(credentials) # return client

class GcpAction(GcpConnect):
        
    # Otwórz arkusz Google Sheets za pomocą nazwy lub ID arkusza
    spreadsheet_id = '1tHr0ppgv03PItKj5KPMx0k5tsyYbpXXEeO1LD3m3s_g'
    sheet_name = 'Gra w słówka'


#sheet = client.open_by_key(spreadsheet_id)#.worksheet(sheet_name)
# Użyj poprawnej nazwy arkusza
#worksheet_name = "Gra w słówka"

gcp = GcpAction()
client = gcp.authorize()
sheet = client.open(gcp.sheet_name).sheet1

# get all
plantas = sheet.get_all_values()

print(plantas)