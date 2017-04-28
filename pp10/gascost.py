#pp10



def gasCost(typeGas,gallons):
    if typeGas.lower() == "regular":
        price = 1.99
    elif typeGas.lower() == "plus":
        price = 2.29
    elif typeGas.lower() == "premium":
        price = 2.59

    total = price * gallons
    return total
    
while True:
    octane = input("Which type of gas would you like: regular, plus, or premium?")
    if octane.lower() == "regular" or octane.lower() == "plus" or octane.lower() == "premium":
        break
    else:
        print("Please choose one of the three types listed!\n\n")


while True:
    gallons = input("How many gallons of gas would you like?")
    gallons = float(gallons)
    if gallons > 0 and gallons <= 1000:
        break
    else:
        print("Please choose an ammount greater then 0 and less then 1000!\n\n")
        
print("Ok, you are interested in,",gallons,"gallons of",octane,"gas.")

print("The total cost is going to be",gasCost(octane,gallons))
