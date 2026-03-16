import json

with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    print('Here are the file contents:')
    print(lines)

# entries = [
#     {
#         'text': 'Make sure to pdractice python every day!',
#     }, {
#         'text': 'Networking is easy in python',
#     }, {
#         'text': 'Python collection types include lists, tuples, sets, and dictionaries',
#     }
# ]

# with open('file_write_demo.json', 'w') as file:
#     # for entry in entries:
#     #     file.write(f"{entry['text']}\n")
#     json.dump(entries, file)

with open('file_write_demo.json', 'r') as file:
    entries = json.load(file)
    print(entries)