x = float(input("Enter first number : "))
y = float(input("Enter second number : "))

option = int(input("What's your choice(1 for +, 2 for -, 3 for x, 4 for / ) ; "))

def add(a,b):
	return a + b

def substract(a,b):
	return a - b

def multi(a,b):
	return a * b

def division(a,b):
	if b == 0:
		return "Can't be divided by ZERO!"

	return a / b

if option == 1:
	print(x, "+", y, "=", add(x,y))

elif option == 2:
	print(x, "-", y, "=", substract(x,y))

elif option == 3:
	print(x, "x", y, "=", multi(x,y))

elif option == 4:
	print(x, "/", y, "=", division(x,y))

else:
	print("Invlaid Choice")
