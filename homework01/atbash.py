def encrypt_atbash(plaintext):
    ciphertext = ""
    for i in plaintext:
        if i.isalpha() and i.isupper():
            if ord(i) < 78:
                ciphertext += chr(ord(i) + (25 - 2 * (ord(i) - 65)))
            else:
                ciphertext += chr(ord(i) - (2 * (ord(i) - 65) - 25))
        elif i.isalpha() and i.islower():
            if ord(i) < 110:
                ciphertext += chr(ord(i) + (25 - 2 * (ord(i) - 97)))
            else:
                ciphertext += chr(ord(i) - (2 * (ord(i) - 97) - 25))
        elif not i.isalpha():
            ciphertext += i
    return ciphertext
