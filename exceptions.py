try:
    age = int(input("Please enter your age: "))
    print(age)
except ValueError:
    print("That was not a number!!!")

print("End of the program!")