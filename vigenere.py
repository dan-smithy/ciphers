#!/usr/bin/env python3

class Rows( object ):
    """
       This class is just used to produce the 
       rows of letters required for a vigenere
       cipher
    """
    
    def __init__( self ):
        self.rows = {}
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.gen_rows()
    
    
    def shift( self, char, key ):
        """
           Essentially a ceaser cipher, which is 
           passed one character and a shift key at a time
        """
        shifted = chr(ord( char ) + key)
        if shifted > 'Z':
            return chr(ord( shifted ) - 26)
        else:
            return shifted

    
    def gen_rows( self ):
        """
           This creates the key-value pairs and inserts
           them into the rows dict
        """
        for i in range( 26 ):
            string = ''
            for char in self.alphabet:
                string += self.shift( char, i )
            self.rows[ self.alphabet[i] ] = string
            


class Main( object ):
    
    def __init__( self ):
        """
           Creates an instance of the Rows class. It also gets the 
           message and the cipher key, converts both to uppercase, 
           removes spaces, and multiplies the key so that it's the 
           same length as the message
        """
        self.char_block = Rows()
        self.text = input("Enter the message: ").upper().replace(" ", "")
        users_key = input("Enter the key: ").upper()
        self.key = (users_key * len( self.text ))[0:len( self.text )]
        self.choice()
        
        
    def choice( self ):
        """
           Simply asks user whether the message will be deciphered 
           or enciphered.
        """
        method = input("Enter e for encipher or d for decipher: ")
        if method == 'e':
            self.encipher()
        elif method == 'd':
            self.decipher()
        else:
            print("Invalid option! Learn to type...")
        
    
    def encipher( self ):
        """
           Loops through both the message and the key. Enciphers each
           character of the message using the key and adds to ciphertext 
           string.
        """
        ciphertext = ""
        for pt, key_char in zip( self.text, self.key ):
            char_index = self.char_block.alphabet.index( pt )
            ciphertext += self.char_block.rows[key_char][char_index]
        print( ciphertext )
        
    
    def decipher( self ):
        """
           Does the opposite of encipher.
        """
        plaintext = ""
        for ct, key_char in zip( self.text, self.key ):
            char_index = self.char_block.rows[key_char].index( ct )
            plaintext += self.char_block.alphabet[char_index]
        print( plaintext )
        
        
        
if __name__ == "__main__":
    run = Main()
            

