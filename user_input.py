name = input("Please enter your name here: ")
print(f"Hello, {name}!!!!!")

# By default, "input" values are strings, if we want a number
# we have to explicitly convert it
age = int(input("What's your age? "))
print(f"You are {age * 12} months old!")

# Boolean values
user_has_long_name = len(name) > 10
print(user_has_long_name)

print("Wow, you have a really long name!")