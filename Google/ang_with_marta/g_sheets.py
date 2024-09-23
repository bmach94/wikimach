import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# cofig file
import yaml

import time #, keyboard
from pynput.keyboard import Key, Controller, Listener

from random import *

from typing import Any

# TODO:
#     Add GUI
#     Add logger
#     Zdania GAME - to finish zdania

class Config():
    """
    Handles loading and processing configuration parameters from a YAML file.
    """

    def load_config(self, filename: str) -> Any:
        """
        Load configuration parameters from a YAML file.

        Parameters:
            filename (str): The name of YAML configuration file

        Returns:
            Any: Parsed YAML content, which can be a dictionary, list, or other data types depending on the YAML structure.
        Raises:
            FileNotFoundError: If the configuration file does not exist.
            yaml.YAMLError: If there's an error in the YAML parsing.
        """

        try:
            with open(filename, 'r') as file:
                config = yaml.safe_load(file)
                return config
        except FileNotFoundError as e:
            print(f"Error: Configuration file '{filename}' not found.")
            raise
        except yaml.YAMLError as e:
            print(f"Error: Failed to parse YAML file '{filename}'.")
            raise

class GcpConnect(Config):
    """
    To connect with GCP.

    Args:
        Config : inherits configuration parameters
    """

    def __init__(self):
        self.config = self.load_config("config_GCP.yaml")
        
    def get_credentials(self):
        """
        Reads the credentials file and creates OAuth2 credentials.
        
        Returns:
            ServiceAccountCredentials: Authorized credentials for Google APIs.
        """
        credentials_file = self.config['GcpConnect']['credentials_file']
        scopes = self.config['GcpConnect']['scope']
        
        # Load credentials from the JSON keyfile
        return ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scopes)
    
    def authorize(self):
        """
        Authorizes and returns a gspread client using the stored credentials.

        Returns:
            gspread.Client: Authorized gspread client.
        Raises:
            FileNotFoundError: If the credentials file does not exist.
            gspread.exceptions.GSpreadException: If the authorization fails.
        """
        try:
            credentials = self.get_credentials()
            return gspread.authorize(credentials)
        except gspread.exceptions.GSpreadException as e:
            print(f"Error: GSpread authorization failed = {e}")
            raise

class Xlsx(Config):
    """
    Handles Xlsx operations.
    
    Args:
        Config : inherits configuration parameters
    """
    
    def __init__(self, gClient):
        
        """
        Args:
            gClient (gspread.Client): Authorized gspread client.            
        """
        
        self.gclient = gClient
        self.config = self.load_config("config.yaml")
   
    def open_sheet(self,worksheet_name):
        """
        Open handler to worksheet.

        Args:
            worksheet_name (string): Name of the worksheet.

        Returns:
            gspread.worksheet.Worksheet: Worksheet handler.
        """
        try:
            return self.gclient.open_by_key(self.config['Xlsx']['DOCUMENT_ID']).worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
class KeyboardActions():

    """
    Handle keyboard actions.
    """
    
    def __init__(self) -> None:
        """
        Initializes the keyboard listener with event handlers for key presses and releases.
        """
        
        self.config = Config().load_config("config.yaml")
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release, suppress=True)
        # connect with GCP    
        client = GcpConnect().authorize()
        # connect with sheet
        xlsx = Xlsx(client)
        self.sheet = xlsx.open_sheet(self.config['Xlsx']['WORKSHEET_SLOWKA_NAME'])
        self.all_values = self.sheet.get_all_values() # dataframe
        self.game = Game(self.all_values[1:])
    
    def on_press(self, key):
        """
        Handle the event when a key is pressed.
        
        Args:
            key : One of the Key members or a KeyCode.
        """
        try:
            if key.char == '1': # Slowka GAME
                self.game.dictionary_game()  # only dictionary words    
        
            elif key.char == '2': # Zdania GAME - to finish!
                print('You pressed {0}'.format(key.char))
                print("Game is not ready.\n")
            
        except AttributeError:
            print('Please, press "1" or "2".\n')

        finally:
            print("Tap '1' or '2' to play again!\n")
            
        
    def on_release(self, key):
        """
        Handle the event when a key is released.

        Parameters:
            key: The key that was released.
        """
    
        try:
            if key == Key.esc:
                # Stop listener
                return False

        except AttributeError:
            pass
        
    def start(self):
        """
        Start the keyboard listener.
        """

        self.game.greeting()
        
        with self.listener:
            self.listener.join()
    
class Game(Config):
    """
    Collects all games related actions.

    Args:
        Config (_type_): _description_
    """
    
    def __init__(self,dictionary):
        self.config = self.load_config("config.yaml")
        self.dictionary = dictionary
        self.size_dict = len(self.dictionary)
        self.user = str()
        # Define a lambda to access elements from self.dictionary
        self.get_dict_word = lambda row, idx: self.dictionary[row][idx+1:idx+3]
        
    def dictionary_game(self):
        """
        Engine of Dictionary Game.
        """

        idx = self.config[self.user][0] # user id


        # Random word from dictionary.
        row = randrange(self.size_dict)
        
        if self.dictionary[row][idx]:
            # Print English word
            print(self.dictionary[row][idx])
            # Break between English word and translation .
            time.sleep(self.config['dict_time_break'])                 
            
            # Print the translations.
            # Print one transaltion or more.
            # If user forgot wrote translation then reminder is written.
            word = self.get_dict_word(row, idx)

            if (word[0] and word[1]) or word[0]:
                print(f"{word[0]} {word[1]}\n")
            elif word[0] == "":
                print('You need to translate on your own :).\n')         
        else:
            print("No word in the dictionary.\n")
            
    def choose_user(self):
        """
        Choose user words colletion.
        """
        print('Choose user words colletion and press "Enter": ')
        
        # Loop used in case if wrong name of user will be choosen
        while True:
            for u in self.config['Users']:
                print(f'{u}')
            self.user = input("Your choice: ")
            print("\n")
            if self.user not in self.config['Users']:
                print("User not known. Choose again.")
                continue
            else:
                break
            
    def greeting(self):
        """
        Print greeting and select user words and the Game.
        """
        print("Welcome! Let's start the Game!")
        self.choose_user()
        print(f"Choose the Game: \n1) Dictionary - selects a random word, after {self.config['dict_time_break']} seconds the translation is displayed\n2) Sentence completion\nTap a number.")
        print("=================================\n")

listener = KeyboardActions()
listener.start()
    

print("THIS IS THE END...")
