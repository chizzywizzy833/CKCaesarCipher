"""
yes and no checker
v1 - set up yes and no checker
"""

# this is a loop that makes it easier for testing
show_instructions = ""
while show_instructions.lower() != "not cipher":

    # Ask the user if they have played before
    show_instructions = input("Have you used a ceaser cipher before? ")

    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no":
        print("display instruction")

    # If input is not yes or no correct user
    else:
        print("please answer yes / no")
