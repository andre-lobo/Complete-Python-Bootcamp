# Build-in function: Enumerate

l = ["a", "b", "c"]

for count, item in enumerate(l):
    print(count)
    print(item)

print()

for count, item, in enumerate(l):
    if count >= 2:
        break
    else:
        print(item)

print()

for count, item in enumerate(l):
    print(count, "-", item)