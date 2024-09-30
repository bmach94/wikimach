
To run game:

1) Create conda environment:

conda create --name=game python==3.9
conda activate game
pip install gspread pandas pyyaml pynput oauth2client

2) Run g_sheets.py script (in wikimach/Google/and_with_marta):

python g_sheets.py

<!-- 
Sprawdzić czy to faktycznie potrzebne:
W launch.json w configuration trzeba dodać:
"cwd" : "${workspaceFolder}/${relativeFileDirname}"
żeby mogło znaleźc pliki otwierane przez skrypt. -->

LINKS:
Google sheet: https://docs.google.com/spreadsheets/d/1De721tDfHyQ_ea1VPlKoK5cEt-3AJtx9SxX2b8PrVOc/edit?gid=0#gid=0
DOCS sheet: https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet
