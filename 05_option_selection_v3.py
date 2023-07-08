"""
Option selection
v1 - creating options
v2 - creating a function
v3-  yes and no checker parameter to make another selection and are you sure option
author- Chisomo Kamphambe
CC CLK 2023
"""


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


choices = " (0) Encrypt a message\n (1) Decrypt a message\n (2) view instruction\n (3) Exit cipher"


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
                # yes and no parameter used here
                confirm = yes_no("are you sure you would exit the program?: ")
                if confirm == "yes":
                    exit()
                else:
                    continue
            else:
                print("Please enter a valid option (0-3)")
        except ValueError:
            print("Invalid input. Please enter an integer.")


print(choices)
option_selection()

# yes and no parameter used here
while True:
    something_else = yes_no("\nwould you like to do something else (Answer with yes or no): ")
    if something_else == "yes":
        print(choices)
        option_selection()
    else:
        # same as the confirm variable on line 44 but, you can't have the same variable name in a function as well as outside the function
        are_you_sure = yes_no("are you sure you would exit the program?")
        break

if are_you_sure == "yes":
    exit()
else:
    print(choices)
    option_selection()
