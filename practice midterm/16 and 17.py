import random




winCount = 0
rollCount = 0
while True:
    xA=random.randint(1,6)
    xB=random.randint(1,6)
    xC=random.randint(1,6)
    xD=random.randint(1,6)
    xE=random.randint(1,6)
  
    if xA == xB and xA == xC and xA == xD and xA ==xE:
        winCount = winCount + 1
    rollCount = rollCount +1
    if winCount == 100000:
        break

prob = winCount/rollCount
answer = 1/prob
answer = int(answer)

print ("You will hit a yahtzee on the first roll about every", answer, "rolls")
print ("It took",rollCount,"rolls to hit",winCount,"wins") 


