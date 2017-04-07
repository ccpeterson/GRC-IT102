# input.py
# This program gives you a random pirate name
# Clinton Peterson
# 06 Apr 2017

#get dat random
import random

#Ask their name
firstName=input("What's your first name?")
lastName=input("What's your last name?")
print(firstName,"please press enter to begin the super-complicated supercomputer process to calculate your pirate name")
input()
input("Beep boop beep. Calculations complete. Press enter to continue.")

#generate name
pirateFirst=["Captain","Stinky-Boot","Peg-Leg","Pludering","Skipper","Stubby","Pirate"]
pirateLast=["Tooth","Jack","McGee","Sparrow","McPirateFace"]
pirateFull=random.choice(pirateFirst)+" "+random.choice(pirateLast)

print(firstName,lastName,"your pirate name is",pirateFull)
input("Press enter to quit.")
