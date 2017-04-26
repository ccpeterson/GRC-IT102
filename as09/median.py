# median.py
# linding the median of a set of numbers
# Clinton Peterson
# 25 April 2017

#Here's the function
def median(listName):
#sorting the list
    listName = sorted(listName)
#Testing that it's sorted 
    print(listName)
#doing the median of a list if it's of even length
    if (len(listName)%2 == 0):
        evenMed1 = listName[(len(listName)//2)-1]
        evenMed2 = listName[(len(listName)//2)]
        evenMed = (evenMed1 + evenMed2)/2
        print(evenMed)
#if it's not even it's odd, so even easier
    else:
        oddMed = listName[(len(listName)//2)]
        print(oddMed)

#Here's the list
thing = [6,4,2,5,3,1,7,9,10,56]
#Why not print it first so I can see that it was sorted
print(thing)
#doing the thing I came to do
median(thing)



	
	
