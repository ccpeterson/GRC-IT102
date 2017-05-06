# potpourri.py
# AS11
# Clinton Peterson
# 02 May 2017

# Stuff I need
import random
import turtle

# Creating the function for prog 2
def areaCalcRect(length,width):
    areaRect = length * width
    return areaRect

# Creating a random color function for prog 3	
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

# Creating a turtle circle funtion for prog 3.
def drawCircle(xLoc, yLoc, fillColor):
    pete.setposition(xLoc, yLoc)
    pete.fillcolor(fillColor)
    pete.begin_fill()
    pete.circle(100)
    pete.end_fill()

# Creating the function for prog 5
def stringReverse(string):
    # An empty string to add characters to from the original
    reverse=""
    z = len(string)
    for i in range(z): 
        reverse += string[z-1-i]
    return reverse

# Letting the user run programs multiple times or quit
playAgain = "yes"
while playAgain.lower() == "yes" or playAgain.lower() == "y":

    # Main menu
    print("Welcome to Clinton's midterm, please pick a program from the menu")
    print("----------")
    print("1 - Program 01: Input and Decisioning Making") 
    print("2 - Program 02: Functions")
    print("3 - Program 03: Loops, Turtle Graphics, and Random")
    print("4 - Program 04: Nested Loops")    
    print("5 - Program 05: Strings and Functions")
    print("6 - Exit")
    print("----------")
    
    # Asking for and validating the menu input

    while True:
        progChoice = input("Which program would you like?")
        
        if progChoice == "1" or progChoice == "2" or progChoice == "3" or progChoice == "4" or progChoice == "5" or progChoice == "6":
            progChoice = int(progChoice)
            break
        else:
            print("Please enter the number of the selection you would like to run and press enter.")

# Program 1
    if progChoice == 1:
        while True:
            dayOfWeek = input ("What day is is today?")

            if dayOfWeek.lower() == "monday" or dayOfWeek.lower() == "mon" or dayOfWeek.lower() == "m":
                print ("Monday's words of encouragement:")
                print ("Go as far as you can see; when you get there, you'll be able to see further.")
                break
            elif dayOfWeek.lower() == "tuesday" or dayOfWeek.lower() == "tues" or dayOfWeek.lower() == "t":
                print ("Tuesday's words of encouragement:")
                print ("You get to decide where your time goes. You can either spend it moving forward,")
                print ("or you can spend it putting out fires. You decide. And if you don't decide,")
                print ("others will decide for you.")
                print ("-Tony Morgan")
                break
            elif dayOfWeek.lower() == "wednesday" or dayOfWeek.lower() == "wed" or dayOfWeek.lower() == "w":
                print ("Wednesday's words of encouragement:")
                print ("Believe you can and you're halfway there.")
                print ("-Theodore Roosevelt")
                break
            elif dayOfWeek.lower() == "thursday" or dayOfWeek.lower() == "thur" or dayOfWeek.lower() == "th":
                print ("Thursday's words of encouragement:")
                print ("Success is the sum of small efforts repeated day in and day out")
                print ("-Robert Collier")
                break
            elif dayOfWeek.lower() == "friday" or dayOfWeek.lower() == "fri" or dayOfWeek.lower() == "f":
                print ("Friday's words of encouragement:")
                print ("Failure is the condiment that gives success its flavor")
                print ("-Truman Capote")
                break
            elif dayOfWeek.lower() == "saturday" or dayOfWeek.lower() == "sat":
                print ("Saturday's words of encouragement:")
                print ("People rarel succeed unless they have fun in what they are doing")
                print ("-Dale Carnegie")
                break
            elif dayOfWeek.lower() == "sunday" or dayOfWeek.lower() == "sun":
                print ("Sunday's words of encouragement:")
                print ("Fall 7 times, stand up 8")
                print ("-Japanese Proverb")
                break
            else:
                print ("Sorry, I didn't understand you.")

# Program 2                
    elif progChoice == 2:
        print ("I will help you perform the incredibly difficult task of finding the area of a rectangle")
        userUnit = input("What is the unit you will be giving me the rectangles dimensions in?")

        # I researched the best way to validate the input, found the While/Try/Except
        userLength = 0
        while True:
          try:
             userLength = float(input("What is the length of the rectangle?"))       
          except ValueError:
             print("Numbers only please.")
             continue
          else:
             break
        userWidth = 0
        while True:
          try:
             userWidth = float(input("What is the width of the rectangle?"))       
          except ValueError:
             print("Numbers only please.")
             continue
          else:
             break

        userArea = areaCalcRect(userLength,userWidth)
        print ("The area of your rectangle is",userArea,userUnit,"squared.")

# Program 3        
    elif progChoice == 3:

        win = turtle.Screen()
        win.setup(1000, 1000)
        win.title("Circles!")
        win.bgcolor("white")
        pete = turtle.Turtle()
        pete.fillcolor("green")
        pete.pencolor("black")
        pete.speed(100)
        pete.penup()
        pete.hideturtle()        

        #Starting in the top left for the first line
        xLoc = -400
        yLoc = 400

        print("Drawing not one, but TWO series of 100 px circles of random color diagonally across a 1000 pixel square window")
        
        for i in range(19):
            random_color = pick_color()
            drawCircle(xLoc,yLoc,random_color)
            xLoc = xLoc + 50
            yLoc = yLoc -50

        #Bottom left for the second line
        xLoc = -400
        yLoc = -400

        for i in range(19):
            random_color = pick_color()
            drawCircle(xLoc,yLoc,random_color)
            xLoc = xLoc + 50
            yLoc = yLoc + 50
            
# Program 4            
    elif progChoice == 4:
        x = 5
        for j in range(5):
            for i in range (x,0,-1):
                print(i," ",end="")
            print("")
            x = x-1

# Program 5 
    elif progChoice == 5:
        userInput = input("Enter text and I'll reverse it: ")
        print (stringReverse(userInput))

# Exit
    elif progChoice == 6:
        break
    else:
        print("This should never happen")


# This happens after a program runs (or when they exit)
    while True:
        print("Want to try another program?")
        playAgain = input()
        if playAgain.lower() == "y" or playAgain.lower() == "yes" or playAgain.lower() == "n" or playAgain.lower() == "no":
            break
        else:
            print("Please type Y or N")

# Goodbye message
print("Thanks for checking it out!")	
input("Press enter to quit.")
