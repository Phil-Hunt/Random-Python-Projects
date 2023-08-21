# Define a function to perform the Caesar cipher encryption/decryption
def caesar_cipher(text, shift):
    encrypted_text = ""
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Shift the character by the specified value within the range of lowercase letters
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shifted_char
        # Check if the character is an uppercase letter
        elif 'A' <= char <= 'Z':
            # Shift the character by the specified value within the range of uppercase letters
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            encrypted_text += char
    
    # Return the encrypted/decrypted text
    return encrypted_text

# Define the main function to take user input and call the caesar_cipher function
def main():
    # Prompt the user to enter the text to encrypt/decrypt
    text = input("Enter the text to encrypt: ")
    
    # Prompt the user to enter the shift value
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    
    # Call the caesar_cipher function to perform the encryption/decryption
    encrypted_text = caesar_cipher(text, shift)
    
    # Display the encrypted/decrypted text
    print("Encrypted/Decrypted text:", encrypted_text)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
