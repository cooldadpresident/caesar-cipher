#inicialization of variables
alphabet = 'abcdef'
print('string', alphabet)
message = ''
rotation = 1

# cycle for each character
for char in alphabet:
    i = ord(char)
    i = i + rotation
    char = chr(i)
    message = message + char
# output
print("ciphered message", message)
input()

