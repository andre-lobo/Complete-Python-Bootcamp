#functions
#def Statements

def my_addition_func(arg1, arg2):	
	"""
	Here is my docstring!
	"""
	return arg1 + arg2

print(my_addition_func(1, 2))
print()

#another function
def greeting(name):
	return "Hello " + name

print(greeting("Andre"))
print()

#another function
def add_num(num1, num2):
	return num1 + num2

x = add_num(5, 3)
print(x)
print()

#another function
def is_prime(num):
	"""
	Check if a number is prime.
	INPUT: A number
	OUTPUT: A print statement whether or not the number is prime.number.
	"""
	for n in range(2, num):
		if num % n == 0:
			print("Not prime")
			break
		else:
			print("This number is prime")

print(help(is_prime))
is_prime(12)