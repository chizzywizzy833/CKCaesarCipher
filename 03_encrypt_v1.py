"""
Encryption component
v1 - set up encryption
"""

# set up variables
user_message = "I have three Cats, two dogs, and a rabbit."
shift = 9


# result placeholder
result = ""

# go through each letter of the message
for letter in user_message:
    # convert letters into the ASCII code
    Ascii_code = ord(letter)
    # Add shift to the ASCII code
    new_Ascii_code = Ascii_code + shift
    # revert the integer back into a string to get encrypted message
    new_letter = chr(new_Ascii_code)
    # append message into the empty string
    result = result + new_letter

print(result)
