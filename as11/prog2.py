def areaCalcRect(length,width):
    areaRect = length * width
    return areaRect

print ("I will help you perform the incredibly difficult task of finding the area of a rectangle")
userUnit = input("What is the unit you will be giving me the rectangles dimensions in?")

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
print ("The area of your rectangle is",userArea,userUnit,"^2")

