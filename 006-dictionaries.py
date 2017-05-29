#dictionaries examples

my_dict = { "key1": "value1", "key2": "value2" }
print(my_dict)
print(my_dict["key1"])

print()

my_dict = { "k1": 123, "k2": 3.4, "k3": "text" }
print(my_dict)

print()

d = {}
d["animal"] = "Dog"
d["answer"] = 42
print(d)

print()

d = {"k1": { "nestkey": { "subnestkey": "value"}}}
print(d["k1"])
print(d["k1"]["nestkey"]["subnestkey"])

print()

d = {}
d = { "k1": 1, "k2": 2, "k3": 3 }
print(d.keys())
print(d.values())
print(d.items())



