"""
yes_no checker component
v1 - set up yes and checker
v2- added .lower it put user input into lowercase
v3 - turn v2 code into a function ,so it is easy to call
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

# call yes and no function
display_instructions = yes_no("Have you used a ceaser cipher before? ")

print("You choose {}".format(display_instructions))
