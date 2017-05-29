#1. Use for, split(), and if to create a Statement that will print out letters that start with "s"
print("*** Resolution of Exercise 1 ***")
st = "Print only the words that start with s in this sentence"

lst = [word for word in st.split() if word[0] == "s"]
print(lst)

#course resolution:
for word in st.split():
	if word[0] == "s":
		print (word)

print("\n*** Resolution of Exercise 2 ***")
#2. Use range() to print all the even numbers from 0 to 10
for x in range(0, 11):
	if (x % 2) == 0:
		print(x)

#course resolution:
lst = list(range(0, 11, 2))
print(lst)

print("\n*** Resolution of Exercise 3 ***")
#3. Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
lst = [number for number in range(1, 51) if number % 3 == 0]
print (lst)

print("\n*** Resolution of Exercise 4 ***")
#4. Go through the string below and if the length of a word is even print "even!"
st = "Print every word in this sentence that has an even number os letters"
for word in st.split():
	if len(word) % 2 == 0:
		print(word)

print("\n*** Resolution of Exercise 5 ***")
#5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print(str(x) + " is FizzBuzz")
	elif x % 3 == 0:
		print(str(x) + " is Fizz")
	elif x % 5 == 0:
		print(str(x) + " is Buzz")
	else:
		print(x)

print("\n*** Resolution of Exercise 6 ***")
#6. Use List Comprehension to creat a list of the first letters of every word in the string below:
st = "Create a list of the first letters of every word in this string"

lst = [word[0] for word in st.split()]
print(lst)