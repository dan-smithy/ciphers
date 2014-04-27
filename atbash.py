ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REV_ALPHABET = ALPHABET[::-1]


def encipher( message ):
    """
       This simply works by finding the position of the char
       in the ALPHABET constant, and then retrieving the same
       index number from REV_ALPHABET.
    """
    ciphertext = ""
    for char in message:
        ciphertext += REV_ALPHABET[ALPHABET.index( char )]
    return ciphertext
    
    
def decipher( message ):
    """
       This is the exact opposite of the encipher() function
    """
    plaintext = ""
    for char in message:
        plaintext += ALPHABET[REV_ALPHABET.index( char )]
    return plaintext
    
    
def main():
    message = input("Please enter message: ").upper().replace(" ", "")
    choice = input("Please enter e for encipher or d for decipher: ")
    
    if choice.upper() == 'E':
        print(encipher( message ))
    elif choice.upper() == 'D':
        print(decipher( message ))
    else:
        print("Invalid option! Learn to type...")
        
        

if __name__ == "__main__":
    main()
