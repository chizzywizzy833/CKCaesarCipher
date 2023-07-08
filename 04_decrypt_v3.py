"""
decryption component
v1 - take encryption component and do the reverse working to make the decryption
v2 - turn v1 into a function
v3 - Get user to only enter negative numbers
"""


def decryption():
    FIRST_LETTER_CODE = ord("A")
    ALPHABET_RANGE = 26
    user_message = input("What is your message you would like to decrypt: ")
    while True:
        try:
            shift = int(input("Enter a negative integer: "))
            if shift < 0:
                break
            else:
                # if user puts in boundary case (positive number) they will be asked to enter a negative one
                print("Invalid input. Please enter a negative integer.")
        except ValueError:
            # if user puts in an unexpected at all they will be asked to put in an integer
            print("Invalid input. Please enter an integer.")
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


decryption()
