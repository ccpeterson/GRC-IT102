# threesort.py
# sorting stuff
# Clinton Peterson
# 27 April 2017

#Need this to make some numbers
import random

totalCountA = 0
totalCountB = 0
totalCountC = 0
print("Generating 3 random integers from 1 to 1000000 and sorting them.")
print("Every compare and every swap count as a move\n")

print("First let's try the method described in the assignment")

for i in range(100000):
    xA=random.randint(1,1000000)
    xB=random.randint(1,1000000)
    xC=random.randint(1,1000000)
    counter = 0
#If the first is bigger then the second, swap them    
    if xA > xB:
        xA, xB = xB, xA
        counter = counter +2
    else:
        counter = counter + 1
#now if the second is bigger then the third, swap them
    if xB > xC:
        xB, xC = xC, xB
        counter = counter +2
    else:
        counter = counter + 1
#checking the first against the second again
    if xA > xB:
        xA, xB = xB, xA
        counter = counter +2
    else:
        counter = counter + 1
    
    totalCountA = totalCountA + counter
        
print("The average number of moves after",(i+1),"iterations is,",totalCountA/(i+1),"\n")
print("Now let's try my method.")

for j in range(100000):
    xD=random.randint(1,1000000)
    xE=random.randint(1,1000000)
    xF=random.randint(1,1000000)
    counter = 0
#Checking the first against the third, this could avoid having to swap a number twice
    if xD > xF:
        xD, xF = xF, xD
        counter = counter + 2
    else:
        counter = counter +1
#now we check the first against the second
    if xD > xE:
        xD, xE = xE, xD
        counter = counter + 2
    else:
        counter = counter +1
#last we check the second against the third
    if xE > xF:
        xE, xF = xF, xE
        counter = counter + 2
    else:
        counter = counter +1
        
    totalCountB = totalCountB + counter
        
print("The average number of moves after",(j+1),"iterations is,",totalCountB/(j+1))

#gloat
if (totalCountB/(j+1)) < (totalCountA/(j+1)):
    print("\nMy alogrithm WINS!!")
else:
    print("\nDoesn't matter what is here because I already know my way wins")

for k in range(100000):
    xG=random.randint(1,1000000)
    xH=random.randint(1,1000000)
    xI=random.randint(1,1000000)
    counter = 0

    if xH > xI:
        xH, xI = xI, xH
        counter = counter + 2
    else:
        counter = counter +1
		
    if xG > xH:
        xG, xH = xH, xG
        counter = counter + 2
    else:
        counter = counter + 1

    if xG > xI:
        xG, xI = xI, xG
        counter = counter + 2
    else:
        counter = counter + 1
         
    totalCountC = totalCountC + counter
        
print("The average number of moves on the experiment, after",(k+1),"iterations is,",totalCountC/(k+1))

