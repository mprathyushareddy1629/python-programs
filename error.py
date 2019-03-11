#error exception.

try:
	a=int(input("give a value"))
	a<3
	print("b=",a/(a-3))

except:
	print("zero error")
else:
	a=3
	print("type error")
finally:
	print("successful")
