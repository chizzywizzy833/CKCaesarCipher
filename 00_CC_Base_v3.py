"""
base component for Caesar Cipher
V0 - skeleton setup
v1 - yes and no checker
v2 - v1 + instructions
v3 - v1 + v2 + encryption
author- Chisomo Kamphambe
CC CLK 2023
"""


# Import libraries go here **************************


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


# variable set up


# main routine goes here ***************
played_before = yes_no("Have used a caesar cipher before? ")


if played_before == "no":
    print(instructions())
    encryption()

else:
    encryption()
