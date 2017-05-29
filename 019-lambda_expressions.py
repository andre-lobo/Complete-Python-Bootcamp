#lambda expressions

#multiple line function
def square(num):
	return num ** 2

print(square(2))
print()

#one line function (It works but it's not pretty)
def another_square(num): return num ** 2

print(another_square(4))
print()

#lambda
square_lambda = lambda num: num ** 2

print(square_lambda(10))
print()

#chech is a number is even
l_even = lambda num: num % 2 == 0
print(l_even(4))
print()

#method version:
def even(num):
	return num % 2 == 0

print(even(4))
print()

#Grabs the first character of a string
l_first = lambda s: s[0]
print(l_first("Hello"))
print()

l_rev = lambda s: s[::-1]
print(l_rev("Hello"))
print()

#sum with two numbers
def adder(x, y):
	return x + y

print(adder(10, 12))
print()

#lamda version:
l_adder = lambda x, y: x + y
print(l_adder(5, 3))
print()

#len check
l_len = lambda item: len(item)
print(l_len("Hello"))