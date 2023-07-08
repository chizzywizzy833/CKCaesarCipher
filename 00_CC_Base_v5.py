"""
base component for Chisomo's Caesar Cipher
V0 - skeleton setup
v1 - yes and no checker
v2 - v1 + instructions
v3 - v1 + v2 + encryption
v4 - v1 + v2 + v3 + decryption
v5 - v1 + v2 + v3 + v4 + option selection
author- Chisomo Kamphambe
CC CLK 2023
"""

# Import libraries go here **************************
import pandas as pd


# functions go here **************************

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes":
            return response

        elif response == "no":
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("****What is a Ceaser Cipher****")
    print("The cipher involves shifting each letter of the plaintext by a certain number of positions in the alphabet.\n"
          "With this cipher you can encrypted a message or decrypt a message.\n"
          "When encrypting a message you will be required to enter a plaintext (message), followed by a positive number you would like to shift it by.\n"
          "When decrypting a message a you will be required to enter a message that has already been encrypted by a caesar cipher.\n"
          "You will also need to know and enter the shift value for that encrypted message.\n"
          "When entering the shift number for a decryption you should also add a negative sign before the number.\n")

    return ""


def encryption():
    # returns the ordinal number for capital letter 'Z' Which is 90
    LAST_LETTER_CODE = ord("Z")
    ALPHABET_RANGE = 26
    user_message = input("What is your message you would like to encrypt: ")
    while True:
        try:
            shift = int(input("enter shift value: "))
            # get user to enter a number between 1 and 20
            if shift < 1 or shift > 20:
                print("Please enter a positive number between 1 and 20.")
            else:
                break
            # if user puts in an unexpected at all they will be asked to put in an integer
        except ValueError:
            print("Invalid input. Please enter a positive number between 1 and 20.")
    result = ""
    for letter in user_message.upper():
        if letter.isalpha():
            Ascii_code = ord(letter)
            new_Ascii_code = Ascii_code + shift
            if new_Ascii_code > LAST_LETTER_CODE:
                new_Ascii_code -= ALPHABET_RANGE
            new_letter = chr(new_Ascii_code)
            result += new_letter
        else:
            result += letter

    print(result)


def decryption():
    FIRST_LETTER_CODE = ord("A")
    ALPHABET_RANGE = 26
    user_message = input("What is your message you would like to decrypt: ")
    while True:
        try:
            shift = int(input("Enter a negative integer: "))
            if shift < 0:
                break
            else:
                # if user puts in boundary case (positive number) they will be asked to enter a negative one
                print("Invalid input. Please enter a negative integer.")
        except ValueError:
            # if user puts in an unexpected at all they will be asked to put in an integer
            print("Invalid input. Please enter an integer.")
    result = ""
    for letter in user_message.upper():
        if letter.isalpha():
            Ascii_code = ord(letter)
            new_Ascii_code = Ascii_code + shift
            if new_Ascii_code < FIRST_LETTER_CODE:
                new_Ascii_code += ALPHABET_RANGE
            new_letter = chr(new_Ascii_code)
            result += new_letter
        else:
            result += letter

    print(result)


def choices(options):
    data = {'Options': options}
    df_one = pd.DataFrame(data)

    # number the options
    df_one.index = range(len(df_one))

    # align the options to the left
    df_one['Options'] = df_one['Options'].apply(lambda x: f'{x:<20}')

    # align the header in the centre
    header = f'{"Options":^20}'
    df_one.columns = [header]

    # print table
    print(df_one)


def option_selection():
    while True:
        try:
            option = int(input("What would you like to do today?: "))
            if option == 0:
                encryption()
                break
            elif option == 1:
                decryption()
                break
            elif option == 2:
                instructions()
                break
            elif option == 3:
                confirm = yes_no("are you sure you would exit the program?: ")
                if confirm == "yes":
                    exit()
                else:
                    continue
            else:
                print("Please enter a valid option (0-3)")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# variables
menu = [
    'Encrypt a message',
    'Decrypt a message',
    'View instructions',
    'Exit cipher'
]

# main routine goes here ***************
played_before = yes_no("Have you used a Caesar cipher before?: ")

if played_before == "no":
    instructions()
    choices(menu)
    option_selection()
else:
    choices(menu)
    option_selection()

while True:
    something_else = yes_no("\nWould you like to do something else?: ")
    if something_else == "yes":
        choices(menu)
        option_selection()
    else:
        are_you_sure = yes_no("Are you sure you want to exit the program?: ")
        if are_you_sure == "yes":
            exit()
        else:
            choices(menu)
            option_selection()
