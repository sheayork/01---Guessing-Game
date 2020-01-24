import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

import random
game_start = input("Hello! Do you want to play a guessing game?   [YES/NO]: ")

if (game_start == "Yes" or game_start == "yes" or game_start == "YES"):
    game_type = input("Let's play a guessing game! What kind do you want?   [NUMBERS/GAME COMPANIES]: ")
    if (game_type == "Numbers" or game_type == "numbers" or game_type == "NUMBERS"):
        number_choice = random.randrange(1, 100)
        
        while True:
            print("I'm thinking of a number between 1 and 100...Guess what number it is!")
            number_guess = input("Guess: ")
            if(int(number_guess) == number_choice):
                print("You got it!")
                break
            if(int(number_guess) > number_choice):
                print("Too high.")
            if(int(number_guess) < number_choice):
                print("Too low.")
            else:
                ("I don't understand your answer. Please try again.")
            

    if (game_type == "Game Companies" or game_type == "game companies" or game_type == "Game companies" or game_type == "GAME COMPANIES"):
        gamecompanyList = ["Nintendo", "Sega", "Ubisoft", "Naughty Dog", "Telltale", "Square Enix", "Konami", "Electronic Arts", "Microsoft Studios", "Sony Computer Entertainment"]
        gamecompanyChoice = random.choice(gamecompanyList)

        while True:
            print("Out of this list, I'm thinking of a random game company...Guess what it is!") 
            gamecompany_guess = input(str(gamecompanyList) + "Guess: ")
            if (gamecompany_guess != gamecompanyChoice):
                print("Try again!")

            else:
                print("You got it! Congrats!")
                break

        else:
            print("I don't understand your answer. Please try again.")
    

elif (game_start == "No" or game_start == "no" or game_start == "NO"):
    print("You're no fun.")

else:
    print("I don't understand your answer. Please try again.")