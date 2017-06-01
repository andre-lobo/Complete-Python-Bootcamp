# Build-in function: Zip

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))
print()

# for looping
a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for pair in zip(a, b):
    print(max(pair))
print()

# using with map
result = list(map(lambda pair: max(pair), zip(a, b)))
print(result)
print()

# list with diferent sizes
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]

result = zip(x, y)

print(list(result))

#with dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

result = zip(d1, d2)
print(list(result))
print()

result = zip (d2, d1.values())
print(list(result))
print()

def switcharoo(d1, d2):
    dout = {}

    for d1key, d2key in zip(d1, d2.values()):
        dout[d1key] = d2key
    
    return dout

print(switcharoo(d1, d2))