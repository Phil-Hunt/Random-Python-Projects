# Caesar Cipher Python Program

The Caesar Cipher Python Program is a simple command-line tool that allows you to encrypt and decrypt messages using the Caesar cipher technique. The Caesar cipher is a basic substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage

1. Clone or download the caesar_cipher.py file.
2. Open a terminal and navigate to the directory where the caesar_cipher.py file is located.
3. Run the program using the following command: python3 caesar_cipher.py
4. The program will prompt you to enter the text to be encrypted or decrypted.
5. You'll also need to provide the shift value. Use a positive value for encryption and a negative value for decryption.


## How It Works

The program consists of two functions:

caesar_cipher(text, shift): This function takes the text and shift as input and returns the encrypted or decrypted text based on the Caesar cipher technique. It iterates through each character in the input text and applies the shift to alphabetic characters (both lowercase and uppercase). Non-alphabetic characters are left unchanged.
main(): This function is the entry point of the program. It prompts the user to enter the text to be encrypted or decrypted and the shift value. It then calls the caesar_cipher function to perform the encryption/decryption and prints the result.

## Example

Suppose you want to encrypt the text "hello" with a shift value of 3. Here's how you would use the program:

Enter the text to encrypt: hello
Enter the shift value (positive for encryption, negative for decryption): 3
Encrypted/Decrypted text: khoor
To decrypt the text "khoor" with a shift value of -3:

Enter the text to encrypt: khoor
Enter the shift value (positive for encryption, negative for decryption): -3
Encrypted/Decrypted text: hello

Feel free to modify the program to add more features or improve its functionality. 
