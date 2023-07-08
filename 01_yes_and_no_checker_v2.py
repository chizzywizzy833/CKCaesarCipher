"""
yes_no checker component
v1 - set up yes and no checker
v2- added .lower it put user input into lowercase
"""

# this is a loop that makes it easier for testing
show_instructions = ""
while show_instructions.lower() != "not cipher":

    # Add .lower so all input can be accepted
    show_instructions = input("Have you used a ceaser cipher before? ").lower()

    if show_instructions == "yes":
        print("program continues")

    elif show_instructions == "no":
        print("display instruction")

    else:
        print("please answer yes / no")
