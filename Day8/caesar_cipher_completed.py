# FINAL PROJECT
import os
from art import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
exit=True
while(exit):
    print (art)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar_cipher(scramble = text , rotation = shift % 19 , action = direction):
        cipher = ""
        for char in scramble :
            if action == "decode": 
                if char not in alphabet :
                    cipher += char
                else :
                    position = alphabet.index(char) - rotation
                    cipher += alphabet[position] 
            elif action == "encode":
                if char not in alphabet :
                    cipher += char
                else :
                    position = alphabet.index(char) + rotation
                    cipher += alphabet[position] 
        os.system("cls")
        print (f"your {action}d message is : {cipher}")

    caesar_cipher()
    ask = input("\nDo you want to exit the program ?\n").lower()
    if ask=="yes":
        exit=False




