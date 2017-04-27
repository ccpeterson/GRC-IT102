import random

totalCountA = 0
totalCountB = 0


print("Generating 3 random integers from 1 to 1000000 and sorting them.")
print("Every compare and every swap count as a move")
print()
print("First let's try the method described in the assignment")

for i in range(1000):
    xA=random.randint(1,1000000)
    xB=random.randint(1,1000000)
    xC=random.randint(1,1000000)
    counter = 0

    if xA > xB:
        xA, xB = xB, xA
        counter = counter +2
    else:
        counter = counter + 1
    if xB > xC:
        xB, xC = xC, xB
        counter = counter +2
    else:
        counter = counter + 1
    if xA > xB:
        xA, xB = xB, xA
        counter = counter +2
    else:
        counter = counter + 1
    
    totalCountA = totalCountA + counter
        
print("The average number of moves after",(i+1),"iterations is,",totalCountA/(i+1))
print()
print("Now let's try comparing the first number to the last one as the first step")

for j in range(1000):
    xD=random.randint(1,1000000)
    xE=random.randint(1,1000000)
    xF=random.randint(1,1000000)
    counter = 0

    if xD > xF:
        xD, xF = xF, xD
        counter = counter + 2
    else:
        counter = counter +1
    if xD > xE:
        xD, xE = xE, xD
        counter = counter + 2
    else:
        counter = counter +1
    if xE > xF:
        xE, xF = xF, xE
        counter = counter + 2
    else:
        counter = counter +1
        
    totalCountB = totalCountB + counter
        
print("The average number of moves after",(j+1),"iterations is,",totalCountB/(j+1))
