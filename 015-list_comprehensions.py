#list comprehensions

l = []

for letter in "word":
	l.append(letter)

print(l)
print()

l = [letter for letter in "Word"]
print(l)
print()

lst = [x ** 2 for x in range(1, 11)]
print(lst)

lst = [number for number in range(11) if number % 2 == 0]
print(lst)