entries = [
    'Make sure to pdractice python every day!',
    'Networking is easy in python',
    'Python collection types include lists, tuples, sets, and dictionaries',
]

def add_new_entry():
    new_entry = input('Enter your new entry: ')
    entries.append(new_entry)
    print('Success!')
    print()

def list_entries():
    for i, entry in enumerate(entries):
        print(f'{i+1}. {entry}')

def delete_entry():
    number_to_delete = int(input('What number list item would you like to delete? '))
    del entries[number_to_delete - 1]

def main_loop():
    print('Welcome to Shaun\'s Amazing Journal Program!')

    while True:
        print('What would you like to do?')
        print('1. Add a new journal entry')
        print('2. List journal entries')
        print('3. Delete a journal entry')
        print('4. Exit')
        user_choice = input('Enter your choice (1-4): ')

        if user_choice == '1':
            add_new_entry() 
        elif user_choice == '2':
            list_entries()
        elif user_choice == '3':
            delete_entry()
        elif user_choice == '4':
            print('Goodbye!')
            break
        else:
            print('That is not a valid option!')

main_loop()