# 8ball.py
# Magic 8 ball
# Clinton Peterson
# 11 Apr 2017

#importing random
import random

#possible answers
possible = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")

#welcome prompt
input("Welcome to the super-accurate MAGIC 8 BALL. To begin press enter.")

#extra points four a loop
playAgain = "yes"
while playAgain == "yes":
#Asking the question
	question = input ("Ask me any question that can answered with a yes or no. ")
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
	print("The answer to your very deep question,(", question, ") is....")
	answer = random.choice(possible)
	print(answer)
	print("")
#asking if they want to continue
	print("Do you want to consult the 8 ball again? (yes or no)")
	playAgain = input()

print("Have a mystical day!")	
input()
	
		



