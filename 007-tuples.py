#list
l = [1, 2, 3]

#tuple is immutable
t = (1, 2, 3)
print(len(t))

print()

t = ("One", 2)
print(t[0])
print(t[1])
print(t[-1])

print("\nReturn index by value")

#return index by value
print(t.index("One"))
print(t.index(2))

print("\nReturn count by value")

#return count by value
t = (1, 1, 2, 3)
print(t.count(1))
print(t.count(2))