#AS 06 Jack Ferrell.py

#Scenario 1
#random color list
#JackFerrell
#April 18 2017

import random
myColorList = ["magenta", "blue", "orange","black","white","purple","violet","green","yellow","pink","crimson","sea green","turquoise","brown","baby blue","grey","indigo","gold","silver","maroon","coral","salmon","azure","tan","orchid","lime","teal","beige","plum","aquamarine","steel blue","goldenrod"]
#list is 32 elements long
userChoice = input("How many colors would you like to print? Input a number from 1 - 32: ")
#define the variable from user choice of number of colors
userChoice=int(userChoice) #the variable needs to be a interger to make this work
for c in range (userChoice): #the range will make the number of colors printed the same as the user input
    print random.choice(myColorList) #random selection from list

#hope you don't mind if some of the random prints are duplicates, I do not know how to make it not duplicate output





    
###Scenario 2
###Names List
###JackFerrell
###April 18 2017
##
##myNamesList = ["Jack" , "Glenn" , "James" , "Sam" , "Hailey" , "Laura"] #define the list
##for i in range (6): #list has 6 elements
##    print  (myNamesList[i])#print the elements of the list
##
##
##
##
##
##
##
##
##
### Scenario 3
### For Loop, Random Centered Color Grid
### JackFerrell
### April 18 2017
##
##
##import turtle
###import random #(did this earlier in code, for copy/ paste uncomment the import)
##
### Set up the window
##win = turtle.Screen()
##win.bgcolor("grey")
##win.title("Loops with Graphics")
##win.setup(500, 500)
##
##colors = ["red", "blue", "green", "yellow", "purple", "#ff6699", "#ffffff","#ff66ff" , "#ff6699" , "#66ff8c" , "#d966ff" , "magenta" , "orange", "violet", "#09f7e4"]
##
### Make a turtle
##bob = turtle.Turtle()
##bob.color("black")
##bob.penup()
##bob.speed(0)
##bob.goto (-150, -150)
##
##for x in range(-3, 3): #range -3 to 3 will give 6 squares
##    for y in range(-3,3):
##        newColor = random.choice(colors) #makes each square random color
##        bob.color(newColor)
##        bob.setposition (x*50, y*50)# size of squares
##        bob.pendown()
##        bob.begin_fill()
##        bob.forward(50)#defining the square
##        bob.left(90)
##        bob.forward(50)
##        bob.left(90)
##        bob.forward(50)
##        bob.left(90)
##        bob.forward(50)
##        bob.left(90)
##        bob.end_fill()
##        bob.penup()
##
##
##
