#!/usr/bin/python3
#Daisy Arnold
#1/27/2019
import pickle
#Data initializaton
datafile = open("game_lib.pickle" , "rb")
library_database = pickle.load(datafile)
datafile.close()
maxkey = 1
for key in library_database.keys():
    maxkey += 1
#constants
MENU_MESSAGE= """
What would you like to do:

1) Add/Edit Games
2) Print All Games
3) Search By Title
4) Remove a Game
5) Save Database
6) Quit
"""
INFO = ['Genre', 'Title',  'Developer', 'Publisher', 'System', 'Rating' , 'release date', 'single/multi?', 'price', 'completion status', 'purchase date', 'notes']
def add_game():
    global maxkey
    user_info = []
    for i in range(len(INFO)):
        print('what is the ', INFO[i], ' of the game to add?: ')
        user_info += input()
    maxkey+= 1 
    library_database[str(maxkey)] = user_info 
    print("running add_game()")
    
def print_all_games():
    #TODO: if the data is not in the library, ask to enter the data
    game_keys = list(library_database.keys())
    for game_key in game_keys:
        for j in range(len(INFO)):
            print(INFO[j] , ': ', library_database[game_key][j])
            
    print("running print_all_games()")
def search_by_title():
    
    print("running search_by_title()")
def remove_a_game():
    print("running remove_a_game()")
def save_database():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(library_database, datafile)
    datafile.close()
def quit():
    print('running_quit')
    exit()
while True:
    choice = input(MENU_MESSAGE)
    if choice == "1":
        add_game()
    elif choice == "2":
        print_all_games()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        remove_a_game()
    elif choice == "5":
        save_database()
    elif choice == "6":
            quit()