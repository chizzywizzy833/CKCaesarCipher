"""
instructions component
print instruction or continue program based on user input
v1 - add yes and no checker to test with instruction component
v2 - make instructions component into function, so it is easy to call
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


def instructions():
    print("****What is a Ceaser Cipher****")
    print("Display instructions")
    return ""


# main routine goes here ***************
played_before = yes_no("Have used a caesar cipher before? ")

print("You choose {}".format(played_before))
