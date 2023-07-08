"""
Option selection
v1 - creating options
"""

# create variable
choices = " (0) Encrypt a message\n (1) Decrypt a message\n (2) view instruction\n (3) Exit cipher"

# print choices
print(choices)

while True:
    try:
        option = int(input("What would you like to do today?: "))
        if option == 0:
            print("run encryption")
            break
        elif option == 1:
            print("run decryption")
            break
        elif option == 2:
            print("display instructions")
            break
        elif option == 3:
            exit()
            break
        else:
            print("Please enter either 0, 1, 2, 3 ")
    except ValueError:
        print("Invalid input. Please enter an integer.")
