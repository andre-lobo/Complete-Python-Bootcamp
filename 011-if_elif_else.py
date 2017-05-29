#if, elif and else examples

if True:
	print("It was True")

print()

x = False

if x:
	print("x was True")
else:
	print("x was False")

print()

loc = "Bank"

if loc == "Auto Shop":
	print("Welcome to the Auto Shop")
elif loc == "Bank":
	print("Welcome to the Bank")
elif loc == "Mall":
	print("Welcome to the Mall")
else:
	print("Where are you?")

print()

person = "Sam"

if person == "Sam":
	print("Hi Sam!")
else:
	print("What's your name?")

