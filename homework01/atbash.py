def encrypt_atbash(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():

            if char.isupper():
                shifted_up = (32 - ((ord(char)-ord('А')) + 1))%32 + ord('А')
                char_code = chr(shifted_up)
                    
            if char.islower():
                shifted_up = (32 - ((ord(char)-ord('а')) + 1))%32 + ord('а')
                char_code = chr(shifted_up)
            ciphertext+=char_code
        else:
            ciphertext+=char
    return ciphertext
print(encrypt_atbash("баба"))