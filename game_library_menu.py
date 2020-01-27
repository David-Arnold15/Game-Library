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
def add_game():
    print("running add_game()")
def print_all_games():
    print("running print_all_games()")
def search_by_title():
    print("running search_by_title()")
def remove_a_game():
    print("running remove_a_game()")
def save_database():
    print("running save_database()")
def quit():
    exit()
    print('running_quit')
choice = input(MENU_MESSAGE)
while True:
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