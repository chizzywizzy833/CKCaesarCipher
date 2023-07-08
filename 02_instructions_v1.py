"""
instructions component
print instruction or continue program based on user input
v1 - add yes and no checker to test with instruction component
"""


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
show_instructions = ""
while show_instructions.lower() != "not cipher":
    # using the yes and no parameter to check user input
    display_instructions = yes_no("Have you played the game before? ")

    if display_instructions == "no":
        print('Display instructions')
        print('program continues')
    else:
        print("Programs continues")
        exit()
