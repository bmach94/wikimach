
To run game:
1) Install conda commend:
  a) on WSL
  # Pobieranie Miniconda
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  
  # Zmienienie uprawnień do uruchamiania skryptu
  chmod +x Miniconda3-latest-Linux-x86_64.sh
  
  # Uruchomienie instalatora
  ./Miniconda3-latest-Linux-x86_64.sh
  # Aktywacja
  source ~/.bashrc
  # Sprawdzenie
  conda --version

  b) on Windows
  Google it :)
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
