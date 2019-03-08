
def func1():
	print("HII")
	print("HELLO")
func1()

#adding a variable
def funcl2(p):
	print("HII")
	print("HELLO","\n",p)
func2("prathyusha")

#with no parameters finding BMI	
def func3(name,height,weight):
	BMI=(height+weight)/2
	print(name,"BMI is",BMI,"\n")
func3("prathu",155,46)



#calling for another function 
def func4(a,b):
	print("for another function")
	x=a+b
	return x

def func5():
	print("now i m going to call for another function")
	q=func5(2,7)
	print("sum is",q)
func5()