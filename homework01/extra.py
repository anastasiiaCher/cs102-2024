"""
Module executing encrypting with the Affine cipher
"""


def encrypt_affine(plaintext, a, b):
    """
    Encrypts plaintext using a Affine cipher.
    """
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                temp = chr(ord("А") + ((ord(i) - ord("А")) * a + b) % 32)
            else:
                temp = chr(ord("а") + ((ord(i) - ord("а")) * a + b) % 32)
            ciphertext += temp
        else:
            ciphertext += i
    return ciphertext
