def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

def main():
    choice = input('Do you want to encrypt (E) or decrypt (D)?\n').lower()
    
    if choice == 'e':
        function = "encrypt"
    elif choice == 'd':
        function = "decrypt"
    else:
        print('Invalid choice')
        main()
        
    text = input(f"What message do you want to {function}?\n")
    custom_key = input(f"What key do you want to use to {function}?\n")
    
    print("Perfect! Press enter to see the result")
    input()
    
    if function == "encrypt":
        print(encrypt(text, custom_key))
    else: 
        print(decrypt(text, custom_key))
    
    exitchoice = input('Do you want to exit? (Y/N)\n').lower()
    if exitchoice == 'n':
        main()
    else:
        print("Press enter to exit.")
        input()
        exit()
main()