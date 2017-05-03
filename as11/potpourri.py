# potpourri.py.py
# Midterm Stuff
# Clinton Peterson
# 02 May 2017

#importing random
import random

def areaCalcRect(length,width):
    areaRect = length * width
    return areaRect

playAgain = "yes"
while playAgain.lower() == "yes" or playAgain.lower() == "y":

    print("Welcome to Clinton's midterm, please pick a program from the menu")
    print("----------")
    print("Program 01: Input and Decisioning Making") 
    print("Program 02: Functions")
    print("Program 03: Loops, Turtle Graphics, and Random")
    print("Program 04: Nested Loops")    
    print("Program 05: Strings and Functions")
    print("----------")
    while True:
        progChoice = input("Which program would you like?")
        
        if progChoice == "1" or progChoice == "2" or progChoice == "3" or progChoice == "4" or progChoice == "5":
            progChoice = int(progChoice)
            break
        else:
            print("Please enter the number of the program you would like to run and press enter.")

    if progChoice == 1:
        print("Do some stuff 1")
    elif progChoice == 2:
        print("Do some stuff 2")
    elif progChoice == 3:
        print("Do some stuff 3")
    elif progChoice == 4:
        print("Do some stuff 4")
    elif progChoice == 5:
        print("Do some stuff 5")
    else:
        print("This should never happen")



    print("Want to try another program?")
    playAgain = input()

print("Thanks for checking it out!")	
input("Press enter to quit.")



