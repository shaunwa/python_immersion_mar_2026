import random

my_list = [100, 300, 200, 400, 500, 600, 700, 700, 700, 100, 300]
my_list[2] = 300
my_list[1] = 200

print(f"The last item is: {my_list[-1]}")
print(f"The second-to-last item is: {my_list[-2]}")

my_list.append(800)

sorted_list = sorted(my_list)

print(my_list)
print(sorted_list)

random.shuffle(sorted_list)
print(sorted_list)

# Slicing
print(my_list[1:4])
print(my_list[:4])
print(my_list[1:])

for x in my_list:
    print(f"{x} is in the list!")