# input.py
# This program gives you a random name
# Clinton Peterson
# 06 Apr 2017

#get dat random
import random

#Ask their name
realName=input("What's your full name?")
print(realName,"please press enter to begin the super-complicated supercomputer process to calculate your pirate name")
input()
input("Beep boop beep. Calculations complete. Press enter to continue.")

#generate name
pirateFirst=["Captain","Stinky-Boot","Peg-Leg","Pludering","Skipper","Stubby","Pirate"]
pirateLast=["Tooth","Jack","McGee","Sparrow","McPirateFace"]
pirateFull=random.choice(pirateFirst)+" "+random.choice(pirateLast)

print(realName,"your pirate name is",pirateFull)
input("Press enter to quit.")
