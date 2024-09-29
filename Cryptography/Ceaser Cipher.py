
//The Caesar Cipher is a monoalphabetic rotation cipher used by Gaius Julius Caesar. Caesar rotated each letter of the plaintext forward three times to encrypt, 
so that A became D, B became E, etc.



alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

message = input("Enter the message to secure:" )  
key = int(input("Enter the key value to secure the message:" ))

length = len(alphabet)
if (length == 26):
    for i in (message):
        position = alphabet.index(i)
        encrypted = position+key
        if (encrypted <= 25):
            print (alphabet[encrypted], end = '')
        else:
            if (encrypted >26):
                condition = encrypted % 26
                print (alphabet[condition], end = '')

else:
    print ("better luck next time")
