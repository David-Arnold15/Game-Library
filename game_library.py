#!/usr/bin/python3
#Daisy Arnold
#1/27/2019
MENU_MESSAGE= """
What would you like to do:

1) Add/Edit Games
2) Print All Games
3) Search By Title
4) Remove a Game
5) Save Database
6) Quit
"""
INFO = ['Title', 'Genre', 'Developer', 'Publisher', 'System','release date', 'number of players', 'price', 'completion status', 'purchase date', 'notes']
library_database = {1:['Title', 'Genre', 'Developer', 'Publisher', 'System','release date', 'single/multi?', 'price', 'completion status', 'purchase date', 'notes']}

def add_game():
    user_info = []
    for i in range(len(INFO)):
        print('what is the ', INFO[i], ' of the game to add?: ')
        user_info += input()
    library_database[title] =user_info 
    print("running add_game()")
    
def print_all_games():
    #TODO: if the data is not
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
    
    print("running save_database()")
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