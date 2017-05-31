# Errors and Exception Handling

try:
    2 + "s"
except TypeError:
    print("There was a type error!")
finally:
    print("Finally this was printed")

print()

try:
    f = open("testefile", "w")
    f.write("Teste write this")
except:
    print("Error in writing to the file!")
else:
    print("File write was a success")

print()

def askint():

    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue;
        else:
            print("Correct, that is an integer!")
            break;
        finally:
            print("Finally block executed!")

        print(val)

askint()