#nested statement and scope

print("*** Enclosing function ***")
name = "This is a global name"

def greet():
	# Enclosing function
	name = "Andre"

	def hello():
		print("Hello", name)

	hello()
greet()

#local variables
print("\n*** Local variables ***")
x = 50

def func(x):
	print("x is", x)
	x = 2
	print("Changed local x to", x)

func(x)
print("x is still", x)

#global statement
print("\n*** Global Statement ***")
x = 50

def function():
	global x
	print("This function is now using the global x")
	print("Because of global x is:", x)
	x = 2
	print("Ran function(), changed global x to", x)

print("Before calling function(), x is", x)
function()
print("Value of x (outside of function()) is:", x)