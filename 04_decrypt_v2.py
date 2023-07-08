"""
decryption component
v1 - take encryption component and do the reverse working to make the decryption
v2 - turn v1 into a function
"""


# function here
def decryption():
    FIRST_LETTER_CODE = ord("A")
    ALPHABET_RANGE = 26
    user_message = input("What is your message you would like to decrypt: ")
    shift = int(input("please enter your shift number: "))
    result = ""
    for letter in user_message.upper():
        if letter.isalpha():
            Ascii_code = ord(letter)
            new_Ascii_code = Ascii_code + shift
            if new_Ascii_code < FIRST_LETTER_CODE:
                new_Ascii_code += ALPHABET_RANGE
            new_letter = chr(new_Ascii_code)
            result += new_letter
        else:
            result += letter

    print(result)


# main routine
decryption()
