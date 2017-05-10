# midterm.py
# Clinton Peterson
# 9 May 2017

#Need random
import random
#Letting the user run programs multiple times or quit
playAgain = "yes"
while playAgain.lower() == "yes" or playAgain.lower() == "y":
    #Introduction
    print ("Welcome to the math test!")
    print ("I'll be asking you 10 random multiplication questions.")
    input ("Press enter to begin")
    correctCount = 0
    #Asking the question 10 times
    for i in range(10):
        x = random.randint(1,9)
        y = random.randint(1,9)
        print ("Question",i+1)
        print(x,y)
        #This is the same input check I had in my potpurri assignment
        while True:
            try:
                answer = float(input("What is the product of these two numbers?"))       
            except ValueError:
                print("Whole numbers only please, try again.")
                print (x,y)
                continue
            else:
                break
        #If they are correct it tells them and increments the counter
        if answer == x * y:
            print("Correct")
            correctCount = correctCount + 1
        #Else they are wrong so it tells them the answer
        else:
            print("I'm sorry the correct answer was", x*y,)
    #Summary of their performance using the counter
    print("You got", correctCount, "correct out of 10")
    if correctCount == 10:
        print("Perfect score, good for you!")
    elif correctCount >=7:
        print("Not bad but you can do better.")
    else:
        print("Keep working to improve.")
    #This is the part where it asks them if they want to go again or quit (with a little input sanitation)
    while True:
        print("Want to try again?")
        playAgain = input()
        if playAgain.lower() == "y" or playAgain.lower() == "yes" or playAgain.lower() == "n" or playAgain.lower() == "no":
            break
        else:
            print("Please type Y or N")
#I hate when the window just closes so I put this at the end of most my programs
print("Thanks for playing")
input("Press enter to quit.")
