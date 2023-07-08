"""
Encryption component
v1 - set up encryption
v2- ignore special characters but still add them to the message
v3- only encrypted using upper case letter
"""
# set up variables
user_message = "I have three Cats, two dogs, and a rabbit."
shift = 9
LAST_LETTER_CODE = 90
ALPHABET_RANGE = 26

# result placeholder
result = ""

# go through each letter of the message
for letter in user_message.upper():
    if letter.isalpha():
        Ascii_code = ord(letter)
        new_Ascii_code = Ascii_code + shift
        # loops back around to the start of upper case Ascii code
        if new_Ascii_code > LAST_LETTER_CODE:
            # range of the alphabet is 26
            new_Ascii_code -= ALPHABET_RANGE 
        new_letter = chr(new_Ascii_code)
        result += new_letter
    else:
        result += letter

print(result)
