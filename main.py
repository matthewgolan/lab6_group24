def print_menu():
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit
''')


keep_looping = True

while keep_looping:
    print_menu()
    user_selection = int(input('Please enter an option: '))
    if user_selection == 1:
        original_password = input('Please enter your password to encode: ')
        encoded_password = ''
        for char in original_password:
            char = int(char)
            char += 3
            char = str(char)
            encoded_password += char
        print('Your password has been encoded and stored! \n')
    elif user_selection == 2:
        pass
    else:
        keep_looping = False
