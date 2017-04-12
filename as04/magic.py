# 8ball.py
# Magic 8 ball
# Clinton Peterson
# 11 Apr 2017

#importing random
import random

#possible answers
possible = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")


#extra points with a loop!
playAgain = "yes"
while playagain == "yes":
#Asking the question
	question = input ("Please ask a yes or no question")
#this is where I get extra extra points	
	print("The magic 8 ball is thinking")
	print("         ____")
	print("     ,dP9CGG88@b,")
	print("   ,IP  _   Y888@@b,")
	print("  dIi  (_)   G8888@b")
	print(" dCII  (_)   G8888@@b")
	print(" GCCIi     ,GG8888@@@")
	print(" GGCCCCCCCGGG88888@@@")
	print(" GGGGCCCGGGG88888@@@@...")
	print(" Y8GGGGGG8888888@@@@P.....")
	print("  Y88888888888@@@@@P......")
	print("  `Y8888888@@@@@@@P'......")
	print("     `@@@@@@@@@P'.......")
	print("")
	input("Press enter to discover the answer")
#spitting out the answer
	answer = random.choice(possible)
	print("The magic 8-Ball says....." + answer)
	print("")
#asking if they want to continue
	print("Do you want to consult the 8 ball again? (yes or no)")
	playagain = input()

print("ok, bye")	
input()
	
		



