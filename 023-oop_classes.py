# OOP - Classes

class Sample(object):
    pass

x = Sample()

print(type(x))
print()

class Dog(object):
    
    # Class Object Attribute
    species = "Mammal"

    def __init__(self, breed, name, fur = True):
        self.breed = breed
        self.name = name
        self.fur = fur

nala = Dog(breed = "Huskie", name = "Nala")
print("Name:", nala.name)
print("Breed:", nala.breed)
print("Species:", nala.species)
print("Fur:", nala.fur)

print()

simba = Dog(breed = "Golden", name = "Simba", fur = False)
print("Name:", simba.name)
print("Breed:", simba.breed)
print("Species:", simba.species)
print("Fur:", simba.fur)