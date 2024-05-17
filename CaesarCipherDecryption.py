'''
Caesars cipher decryption
'''
cipheredText = str(input('Message to decrypt '))


print('Plaintext in lowercase', cipheredText)
plainText = ''
key = 3



# iterate through each character in the plaintext string.

for char in cipheredText:
    i = ord(char)
    i = i - key
    if (i > ord('z')):
        i = i - 26
        
    # shift the ASCII value of the character by the key value (3 in this case).
    char = chr(i)
    
    # Subtract the decrypted character to the cipheredtext string.
    plainText = plainText + char
    
# output
print('Plaintext', plainText)