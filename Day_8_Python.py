#Caesar Cipher
# def greet():
#     print('How are you?')
#     print("That's good")
#     print("I'm doing good as well, thanks")

# greet()

# #Functions that allow for input
# #                   Paramters
# def greet_with_name(name, last_name):
#     name = input("What is your First name?\n")
#     last_name = input("What is your last name?")
#     print(f"Hello: {name} {last_name}")

# #              Arguments
# greet_with_name('', '')

#My Third attempt Caesar Cipher

def caesar_Cipher(message, encoder):
    encode_or_decode = input("Would you like to encode or decode?\n")
    message = input("What message would you like to encode?\n")
    encoder = int(input("Which Caesar Cipher number would you like to encode with?\n"))
    alphabet_encoder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded_message = ''
    number = 0
    for letter in message.lower():
        if letter in alphabet_encoder and encode_or_decode == 'encode':
            number = alphabet_encoder.index(letter)
            encoded_message += alphabet_encoder[encoder + number]
        elif letter in alphabet_encoder and encode_or_decode == 'decode':
            number = alphabet_encoder.index(letter)
            encoded_message += alphabet_encoder[number - encoder]
    print(encoded_message)

caesar_Cipher('', 0)

#Caesar Cipher CHATGPT Answer
# def caesar_cipher(text, shift, mode='encrypt'):
#     result = ''
#     for char in text:
#         if char.isalpha():
#             shift_amount = shift if mode == 'encrypt' else -shift
#             base = ord('A') if char.isupper() else ord('a')
#             # Shift within alphabet bounds
#             result += chr((ord(char) - base + shift_amount) % 26 + base)
#         else:
#             result += char  # Non-alphabetic characters stay the same
#     return result

# # Example usage
# message = input("Enter your message: ")
# shift = int(input("Enter shift amount (e.g., 3): "))
# mode = input("Encrypt or Decrypt? ").lower()

# if mode in ['encrypt', 'decrypt']:
#     output = caesar_cipher(message, shift, mode)
#     print(f"\n{mode.title()}ed message: {output}")
# else:
#     print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

#Caesar Cipher Teacher answer
