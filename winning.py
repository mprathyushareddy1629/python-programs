import random
i=0
while i<2:
	d=6

	r= input("press r to roll the dice,q to quit:")
	if d=="r":
		print("you got:",d)
	d=d/2

	r= input("press r to roll the dice,q to quit:")
	if d=="r":
		print("you got:",d)
	d=d+1

	i=i+1
	print("you won!!!")

	exit()