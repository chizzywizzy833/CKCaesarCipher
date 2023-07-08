"""
interactive instruction
v1 - set up skeleton of interactive instructions
v2 - make functions, so it is easy to call in the base component
v3 - imported time
"""

import time


def encryption_demo():
    LAST_LETTER_CODE = ord("Z")
    ALPHABET_RANGE = 26

    user_name = input("Hello, please enter your name to start the demonstration: ").lower()
    print("\nHello", user_name, "welcome to the encryption demo")

    encryption_demo_message = input(
        "\nTo start an encryption, you will need to enter a message. Please enter 'hello' followed by your name: ").lower()

    while True:
        if encryption_demo_message == "hello " + user_name:
            break
        else:
            print("\nPlease enter 'hello' followed by your name. For example, 'hello", user_name + "'.")
            encryption_demo_message = input(
                "To start an encryption, you will need to enter a message. Please enter your name: ").lower()

    while True:
        try:
            encryption_demo_shift = int(input("Please enter your shift number: "))
            # get user to enter a number between 1 and 20
            if encryption_demo_shift < 1 or encryption_demo_shift > 20:
                print("Invalid input. Please enter a positive number between 1 and 20.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive number between 1 and 20.")

    result = ""
    print("Original message: " + encryption_demo_message)
    time.sleep(1)
    print("Shift: " + str(encryption_demo_shift))
    time.sleep(1)
    for letter in encryption_demo_message.upper():
        if letter.isalpha():
            ascii_code = ord(letter)
            new_ascii_code = ascii_code + encryption_demo_shift
            if new_ascii_code > LAST_LETTER_CODE:
                new_ascii_code -= ALPHABET_RANGE
            new_letter = chr(new_ascii_code)
            result += new_letter

            # Print each step of the encryption process
            print(f"Letter: {letter} -> Encrypted: {result}")

            # Sleep/wait for 1 second before proceeding to the next step
            time.sleep(1)
        else:
            result += letter

    print("Encrypted message: " + result)


def decryption_demo():
    print("OMQEMD OUBTQD")

    while True:
        # ask user to put in message above if not ask question again
        decryption_demo_message = input("To start decryption, enter the text above into the space provided: ")
        if decryption_demo_message == "OMQEMD OUBTQD":
            break
        else:
            print("Invalid input. Please enter the provided text.")

    while True:
        decryption_demo_shift = input("To decrypt the message, enter the shift value -12: ")
        try:
            shift = int(decryption_demo_shift)
            if shift == -12:
                break
            else:
                print("Invalid input. Please enter -12 as the shift value.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    FIRST_CHAR_CODE = ord("A")
    ALPHABET_RANGE = 26
    user_message = decryption_demo_message

    print("Original message: " + decryption_demo_message)
    time.sleep(1)
    print("Shift: " + str(decryption_demo_shift))
    time.sleep(1)

    result = ""
    for letter in user_message.upper():
        if letter.isalpha():
            Ascii_code = ord(letter)
            new_Ascii_code = Ascii_code + shift
            if new_Ascii_code < FIRST_CHAR_CODE:
                new_Ascii_code += ALPHABET_RANGE
            new_letter = chr(new_Ascii_code)
            result += new_letter
            # Print each step of the decryption process
            print(f"Letter: {letter} -> Decrypted: {result}")

            # Sleep for 1 second before proceeding to the next step
            time.sleep(1)
        else:
            result += letter
    print("Encrypted message: " + result)


# main routine
encryption_demo()

decryption_demo()
