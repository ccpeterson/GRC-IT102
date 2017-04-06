# input.py
# This program requests info and spits out an address
# Clinton Peterson
# 06 Apr 2017

firstName = input("Please input your first name:  ")
lastName = input("Please input your last name:  ")
streetAddress = input("Please input your street address:  ")
city = input("Please input your city:  ")
state = input("Please input your state's two letter abbriviation:  ")
zip = input("Please input your ZIP code:  ")

input("Thanks, press enter to see what a letter addressed to you would look like")

print(firstName+lastName)
print(streetAddress)
print(city+state+zip)
