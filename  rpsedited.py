import random
l=["r","p","s"]

#take input from the user
u=input("enter the choice,enter q to quit")

#to quit
if u=='q':
	print("game over")
	exit()

#input from the computer
c=random.choice(l)
print("computer chooses",c)

#compare the user and the computer choice
if u==c:
	print("tie")

elif u=="r" and c=="p":
	print("comp wins")
elif u=="s" and c=="r":
	print("comp win")
elif u=="p" and c=="s":
	print("comp wins")

else:
	print("you win")

