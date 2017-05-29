#handling files

file_path = "C:\\Andre\\Work\\Python\\Files\\file_test.txt"

f = open(file_path)
print(f.read())

f.seek(0)

print(f.readlines())

print()

for line in open(file_path):
	print(line)