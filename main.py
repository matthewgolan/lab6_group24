# Matthew Golan

# Defines function for use in loop.
def print_menu():
    """Prints program menu"""
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit
''')

# Moved encoding process into a function to conform with the style of partners code.
def encoder(original_password):
    """Encodes password"""
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
    return encoded_password

def decoder(encoded_password):
    original_password = ''
    new_element = ''
    for element in encoded_password:
        if int(element) in range(9, 2, -1):
            new_element = int(element) - 3
        elif int(element) == 2:
            new_element = 9
        elif int(element) == 1:
            new_element = 8
        original_password += str(new_element)
    return original_password

# Assigns variable as true so program enters loop.
keep_looping = True

while keep_looping:
    # Accesses the print function.
    print_menu()
    user_selection = int(input('Please enter an option: '))
    # Initiates encoding processes.
    if user_selection == 1:
        original = input('Please enter your password to encode: ')
        encoded = encoder(original)
        print('Your password has been encoded and stored! \n')
    elif user_selection == 2:
        original_password = decoder(encoded)
        print(f'The encoded password is {encoded}, and the original password is {original_password}')
        print()
    # Exits loop when user selects 3.
    else:
        keep_looping = False
