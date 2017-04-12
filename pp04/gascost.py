# gascost.py
# This computes gas cost
# Clinton Peterson
# 11 Apr 2017

gasCostInput = input("How much is the gas per gallon?")
gasCost = float(gasCostInput)
gasVolInput = input("How mumany gallons you get?")
gasVol = float(gasVolInput)

price = gasCost * gasVol

print ("The total cost of your gas purchase is equal to $" + str(round(price, 2))+ ".")
input()

