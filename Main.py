import random
import os

"""
Characters Allowed
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=

Characters Allowed In Domain
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-
length => 63

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 -
"""

ALLOWEDCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789- "

KEY = "UhOo34q4vz-pTLop7lgyyZ8flroHbbVvne3-j5N0Ngf5O0c88kTKTQqd0cql913gZPKafTQ4CxxjivqtNLYf98uiRQKKF8wY5X-knU0yPLmAUtb2fLQit7zQ5C5e"
KeyLength = 2

Message = "Message here"

def GenerateKey(KeyLength: int):
    x = ''
    for i1 in range(64):
        y = ''
        for i2 in range(KeyLength):
            z = random.randrange(0,65)
            z = ALLOWEDCHARS[z:z+1]

            y = y + str(z)
        x = x + y
    return x

def Encript(Key: str, KeyLength: int, Message: str):
    x = ''
    for i1 in Message:
        Match : int
        for i2 in ALLOWEDCHARS:
            if i1 == i2:
                Match = int(ALLOWEDCHARS.index(i2))
                break
        x = x + Key[Match:Match+KeyLength]
    return x

def Decript(Key: str, KeyLength: int, Encripted: str):
    x = ''
    for i in range(int(len(Encripted) / KeyLength)):
        Letter = Encripted[1*(i * KeyLength) : KeyLength*(i+1)]
        LetterIndex = Key.find(Letter)
        x = x + str(ALLOWEDCHARS[LetterIndex:LetterIndex+1])
    return x

EncriptedMessage = Encript(KEY, KeyLength, Message)
DecriptedMessage = Decript(KEY, KeyLength, EncriptedMessage)

print("Key Used: " + KEY)
print("Encripted Message: " + EncriptedMessage)
print("Decripted Message: " + DecriptedMessage)
print(">------<")
print("Original Message: " + Message + "\nIf decripted message and original message are not the same try a different key")

def Main():
    print("Encrypt, Decrypt, Generate  Key?")
    allowed = ["encrypt", "e", "decrypt", "d", "generate", "key", "generate key", "gk", "g", 'k']
    Doing = ''

    key = ""
    key_len = 0
    message = ""

    while not Doing in allowed:
        Doing = input().lower()
    if Doing == "encrypt" or Doing == "e":
        key = input("Key: ")
        key_len = int(input("Key Length: "))
        message = input("Message: ")

        Encripted = Encript(key, key_len, message)
        print(Encripted)

    elif Doing == "decrypt" or Doing == "d":
        key = input("Key: ")
        key_len = int(input("Key Length: "))
        encripted = input("Encripted Message: ")

        Decripted = Decript(key, key_len, encripted)
        print(Decripted)

    elif Doing == "generate" or Doing == "g" or Doing == "key" or Doing == "k" or Doing == "generate key" or Doing == "generatekey" or Doing == "gk" or Doing == "g k":
        key_len = int(input("Key Length: "))

        Generated = GenerateKey(key_len)
        print(Generated)
    
    Doing = input("quit?: ")
    if Doing == "quit" or Doing == "q" or Doing == "y" or Doing == "yes":
        quit()
    else:
        Main()

Main()