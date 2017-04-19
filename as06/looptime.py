# looptime.py
# Intro to For Loop
# Clinton Peterson
# 18 April 2017

# First scenario

import random
colorList = ["red","blue","green","yellow","black","white","purple","brown","gray","magenta","orange","violet","pink","turquoise","sky blue","indigo","gold","silver","maroon","coral","salmon","tan","lime","teal","beige"]
print("I will print you a random list of colors")
userChoice = input("How long would you like the list? Input a number from 1 - 20: ")
#make it an int
userChoice=int(userChoice)
#loop it up
for i in range (userChoice): #the range will make the number of colors printed the same as the user input
    print (i)
	
