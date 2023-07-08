"""
base component for Caesar Cipher
V0 - skeleton setup
v1 - yes and no checker
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


# main routine goes here ***************
played_before = yes_no("Have used a caesar cipher before? ")

if played_before == "no":
    print("display instructions")
    print("program continues")
else:
    print("Program continues")
