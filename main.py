# Defines function for use in loop.
def print_menu():
    """Prints program menu"""
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit
''')

# Assigns variable as true so program enters loop.
keep_looping = True

while keep_looping:
    # Accesses the print function.
    print_menu()
    user_selection = int(input('Please enter an option: '))
    # Initiates encoding processes.
    if user_selection == 1:
        original_password = input('Please enter your password to encode: ')
        # Creates an empty string for use in loop.
        encoded_password = ''
        # Converts each character to an integer, adds three, converts back to a string, and adds to encoded_password.
        for char in original_password:
            char = int(char)
            char += 3
            # Accounts for two-digit numbers
            if char == 10:
                char = 0
            elif char == 11:
                char = 1
            elif char == 12:
                char = 2
            char = str(char)
            encoded_password += char
        print('Your password has been encoded and stored! \n')
    elif user_selection == 2:
        pass
    # Exits loop when user selects 3.
    else:
        keep_looping = False
