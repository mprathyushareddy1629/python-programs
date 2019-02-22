import random
#this is a dictionary
d={2:12,10:15,16:20,24:36,38:39,41:48,52:54,59:61,62:68,73:76,87:92,96:97}

p=random.choice([10,2,52,68,91,97])

print("you got",p)

if p in d:
	if p>d[p]:
		print("snake")
	else:
		print("ladder")

	print("you can go to",d[p])