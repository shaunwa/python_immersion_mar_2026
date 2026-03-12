count = int(input("How many times should I repeat? "))

for i in range(count):
    print(f'Hello {i+1}!')

x = [1, 2, 3, 4, 5]

for i in x:
    print(f'The list contains: {i}')

name = input("Enter your name: ")

while len(name) == 0:
    print("Don't leave that value blank!")
    name = input("Enter your name: ")