# median.py
# a function that finds the median of a set of numbers
# Clinton Peterson
# 25 April 2017

#Here's the function, it expects a list of numbers
def median(listName):
#sorting the list
    listName = sorted(listName)
#Testing that it's sorted 
    print("Here's the list, but sorted.",listName)
#Finding the median of the list if it's of even length
#Gotta find the two middle numbers and average them
    if (len(listName)%2 == 0):
        evenMed1 = listName[(len(listName)//2)-1]
        evenMed2 = listName[(len(listName)//2)]
        evenMed = (evenMed1 + evenMed2)/2
        print("The Median of that list is",evenMed)
#If it's not even it's odd, so even easier
#Just finding the middle number
    else:
        oddMed = listName[(len(listName)//2)]
        print("The Median of that list is",oddMed)

#Here's two lists
thingEven = [6,4,2,5,3,9,10,56]
thingOdd = [6,4,7,2,5,3,1,7,9,106,99]

#showing the list of numbers before we run it through the function
print("Here's the list of numbers from the odd numbered list",thingOdd)
#doing the thing I came to do
median(thingOdd)

print()

#Do it again but with a different list
print("Here's the list of numbers from the even numbered list",thingEven)
#doing the thing I came to do
median(thingEven)
	
	
