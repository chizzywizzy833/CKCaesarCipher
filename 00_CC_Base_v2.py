"""
base component for Caesar Cipher
V0 - skeleton setup
v1 - yes and no checker
v2 - v1 + instructions
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


# main routine goes here ***************
played_before = yes_no("Have used a caesar cipher before? ")

if played_before == "no":
    print(instructions())
    print("program continues")
else:
    print("Program continues")
