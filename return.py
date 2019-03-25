x=float(input("enter the value of a"))
y=float(input("enter the value of b"))
z=float(input("enter the value of c"))
def sum(x,y,z):
	if x==y:
		return (0)
	elif x==z:
		return (0)
	elif z==y:
		return (0)
	else :
		return (x+y+z)
	
a=sum(x,y,z)
print(a)