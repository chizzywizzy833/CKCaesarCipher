"""
Encryption component
v1 - take encryption component and do the reverse working to make the decryption
"""

# returns the ordinal number for capital letter 'A' Which is 65
FIRST_LETTER_CODE = ord("A")
ALPHABET_RANGE = 26
user_message = "R QJEN CQANN LJCB, CFX MXPB, JWM J AJKKRC."
# shift value for decryption
shift = -9

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
