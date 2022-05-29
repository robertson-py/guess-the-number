import random
import sys

#Define variables "tries" and 'global_user_option'
tries = 0
global_user_option = 0

#Define dictionaries "difficulties" and "options" to choose the game level
difficulties = {1:"easy", 2:"normal", 3:"hard"}
options = {"easy": 3, "normal": 5, "hard":7}

#Define the functions of the game
def random_number(difficulty):
    """Function to choose the difficulty of the game"""

    if difficulty == "easy":
        print("Guess a number between 0 and 10")
        print("You've got 3 tries")
    elif difficulty == "normal":
        print("Guess a number between 0 and 25")
        print("You've got 5 tries")
    elif difficulty == "hard":
        print("Guess a number between 0 and 50")
        print("You've got 7 tries")
    else:
        print("Wrong option, try again.")

def main_function(user_option):
    """Function that manages the variables, input and output of the game"""

    random_number(difficulties[user_option])        #Run the 'random_number' function to pick the level from user's input
    tries = options[difficulties[user_option]]      #Add to 'tries' a value based on user's input

    #Add to 'guess' a random number based on the difficulty
    if tries == 3:
        guess = random.randint(0, 10)
    if tries == 5:
        guess = random.randint(0, 25)
    if tries == 7:
        guess = random.randint(0, 50)

    #Main loop of the game
    while tries > 0:
        user = int(input("Take a chance, tap a number: "))
        if user == guess:                           #Win condition
            print("Great ! you guessed the number")
            break
        else:
            tries -= 1
            if tries == 0:
                print("Game over")
            else:
                print("Try again, you've got " + str(tries) + " tries")
                if user < guess:
                    print("The number is bigger")
                else:
                    print("The number is lower")
    
    #Loop if the user wants to play again or exit the game
    while True:
        check = input("Do you want to play again?(Y/N)").upper()
        if check == "Y":
            display_menu()
        elif check == "N":
            sys.exit()
        else:
            print("Wrong choice, try again.")

def display_menu():
    """Function that displays the menu to start the game"""
    while True:
        try:
            global_user_option = int(input("Please, choose an option(1/2/3):"))
            if global_user_option == 1:
                main_function(global_user_option)
            elif global_user_option == 2:
                main_function(global_user_option)
            elif global_user_option == 3:
                main_function(global_user_option)
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, try again.")

display_menu()