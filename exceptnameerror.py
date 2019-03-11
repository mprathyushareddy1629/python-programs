#name error in exceptional
try:
	#p=10
	print(p)
	raise NameError
except NameError:
	print("p is not defined")
else:
	print("reddy")
finally:
	print("bye..!!")