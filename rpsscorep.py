import random
l=["r","p","s"]
d={"r":"rock","p":"paper","s":"scissors"}
for x in d:
	print(x,d[x])
us=0
cs=0

#take input from the user
u=input("enter the choice,enter q to quit")
print("user chooses",u)

#input from the computer
c=random.choice(l)
print("computer chooses",c)

#compare the user and the computer choice
if u==c:
	#print("tie")
	cs=us
elif u=="r" and c=="p":
	#print("comp wins")
	print("score is", cs==cs+1)
elif u=="s" and c=="r":
	#print("comp win")
	print("score is",cs==cs+1)
elif u=="p" and c=="s":
	#print("comp wins")
	print("score is",cs==cs+1)

else:
	#print("you win")
	us=us+1
#to quit
if u=="q":
	print("game over")
	print("computer and user score is",cs,us)
if cs>us:
	print("computer wins",cs,us)
elif us>cs:
	print("user wins",cs,us)
else:
	print("its a tie",cs,us)

	exit()

