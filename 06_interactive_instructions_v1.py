"""
interactive instruction
v1 - set up skeleton of interactive instructions
"""
# Encryption demo
user_name = input("Hello, please enter your name to start the demonstration: ").lower()
print("\nHello", user_name, "welcome to the encryption demo")

encryption_demo_message = input(
    "\nTo start an encryption you will need to enter a message a plain text message. Please enter 'hello' followed by your name: ").lower()

while True:
    if encryption_demo_message == "hello " + user_name:
        break
    else:
        print("\nplease enter you hello followed by your name eg hello", user_name)
        encryption_demo_message = input(
            "To start an encryption you will need to enter a message. Please enter your name: ")

print("start Encryption demo")

# Decryption demo
decryption_demo_answer = "OMQEMD OUBTQD"

print("OMQEMD OUBTQD")

encryption_demo_message = input("To start an decryption enter the text above into the space provided:")
decryption_demo_shift = input("to decrypted the message enter the shift value -12:")
print("start decryption demo")
