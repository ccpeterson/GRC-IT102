

def stringReverse(string):
    reverse=""
    l = len(string)
    for i in range(l):
        reverse += string[l-1-i]
    return reverse

userInput = input("Enter text and I'll reverse it: ")

print (stringReverse(userInput))
