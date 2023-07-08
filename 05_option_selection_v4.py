"""
Option selection
v1 - creating options
v2 - creating a function
v3-  yes and no checker parameter to make another selection and are you sure option
v4 - imported pandas to format options
author- Chisomo Kamphambe
CC CLK 2023
"""

# libraries
import pandas as pd


# functions here
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
                print("Run encryption")
                break
            elif option == 1:
                print("Run decryption")
                break
            elif option == 2:
                print("Display instructions")
                break
            elif option == 3:
                confirm = yes_no("Are you sure you want to exit the program? (Answer with yes or no): ")
                if confirm == "yes":
                    exit()
                else:
                    continue
            else:
                print("Please enter a valid option (0-3)")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Variable setup
menu = [
    'Encrypt a message',
    'Decrypt a message',
    'View instructions',
    'Exit cipher'
]

choices(menu)
option_selection()

while True:
    something_else = yes_no("\nWould you like to do something else? (Answer with yes or no): ")
    if something_else == "yes":
        choices(menu)
        option_selection()
    else:
        are_you_sure = yes_no("Are you sure you want to exit the program? (Answer with yes or no): ")
        if are_you_sure == "no":
            choices(menu)
            option_selection()
        else:
            exit()
