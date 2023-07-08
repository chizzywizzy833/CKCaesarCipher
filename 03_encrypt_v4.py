"""
Encryption component
v1 - set up encryption
v2- ignore special characters but still add them to the message
v3- only encrypted using upper case letter
v4- turn v3 into a function
"""

# set up variables
LAST_LETTER_CODE = 90
ALPHABET_RANGE = 26


# Function here
def encryption():
    user_message = input("What is your message you would like to encrypt: ")
    shift = int(input("please enter your shift number: "))
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
