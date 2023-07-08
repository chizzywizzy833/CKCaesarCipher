"""
Encryption component
v1 - set up encryption
v2- ignore special characters but still add them to the message
v3- only encrypted using upper case letter
v4- turn v3 into a function
v5-Get user to only enter positive numbers between 1 and 20
"""


def encryption():
    # returns the ordinal number for capital letter 'Z' Which is 90
    LAST_LETTER_CODE = ord("Z")
    ALPHABET_RANGE = 26
    user_message = input("What is your message you would like to encrypt: ")
    while True:
        try:
            shift = int(input("enter shift value: "))
            # get user to enter a number between 1 and 20
            if shift < 1 or shift > 20:
                print("Please enter a positive number between 1 and 20.")
            else:
                break
            # if user puts in an unexpected at all they will be asked to put in an integer
        except ValueError:
            print("Invalid input. Please enter a positive number between 1 and 20.")
    result = ""
    for letter in user_message.upper():
        if letter.isalpha():
            Ascii_code = ord(letter)
            new_Ascii_code = Ascii_code + shift
            if new_Ascii_code > LAST_LETTER_CODE:
                new_Ascii_code -= ALPHABET_RANGE
            new_letter = chr(new_Ascii_code)
            result += new_letter
        else:
            result += letter

    print(result)


# main routine

encryption()
