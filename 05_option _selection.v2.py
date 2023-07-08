"""
Option selection
v1 - creating options
v2 - creating a function
author- Chisomo Kamphambe
CC CLK 2023
"""

choices = " (0) Encrypt a message\n (1) Decrypt a message\n (2) view instruction\n (3) Exit cipher"
print(choices)


# function here
def option_selection():
    while True:
        try:
            option = int(input("What would you like to do today?: "))
            if option == 1:
                print("run encryption")
                break
            elif option == 2:
                print("run decryption")
                break
            elif option == 3:
                print("display instructions")
                break
            elif option == 4:
                exit()
                break
            else:
                print("Please enter either 1, 2, 3, 4 ")
        except ValueError:
            print("Invalid input. Please enter an integer.")


option_selection()
