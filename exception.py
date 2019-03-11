
#exceptional 
try:
	p=1
	print(p)
except:
	print("p is not defined")
else:
	print("heyy")
finally:
	print("bye..!!!")

#exceptional with name error
try:
	q=1
	print(q)
	raise NameError
except NameError:
	print("u have not defined q")
except:
	print("unsuccess")
else:
	print("hello")
finally:
	print("success")
