'''
Caesars cipher
'''
plaintext = input('Message to cipher ')

#Convert the plaintext string to lowercase to ensure consistency.

plaintext = plaintext.lower()
print('Plaintext in lowercase', plaintext)
message = ''
key = 3

    

# iterate through each character in the plaintext string.

for char in plaintext:
    i = ord(char)
    i = i + key
    if (i > ord('z')):
        i = i - 26
    # shift the ASCII value of the character by the key value (3 in this case).

    char = chr(i)
     # Append the encrypted character to the message string.
    message = message + char
    
# output
print('Ciphertext', message)