"""
Encryption component
v1 - set up encryption
v2- ignore special characters but still add them to the message
"""
# set up variables
user_message = "I have three Cats, two dogs, and a rabbit."
shift = 9

# result placeholder
result = ""

# go through each letter of the message
for letter in user_message:
    """check to see if letter in message is 
    part of the alphabet if not returns as boolean 
    and ignores characters"""
    if letter.isalpha():
        Ascii_code = ord(letter)
        new_Ascii_code = Ascii_code + shift
        new_letter = chr(new_Ascii_code)
        result += new_letter
    else:
        """adds the original character e.g. 
        comma and space back into the 
        encrypted message"""
        result += letter

print(result)
