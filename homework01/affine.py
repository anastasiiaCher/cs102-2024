def encrypt_affine(plaintext, a, b):
    """
    Encrypts plaintext using an Affine cipher.

    >>> encrypt_affine("PYTHON", 3, 5)
    'YZKAVS'
    >>> encrypt_affine("python", 7, 12)
    'nypjgz'
    >>> encrypt_affine("Python3.6", 5, 12)
    'Jcdvez3.6'
    >>> encrypt_affine("", 2, 3)
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if "A" <= char <= "Z":
            ord_new_char = ord("A") + (a * (ord(char) - ord("A")) + b) % 26
        elif "a" <= char <= "z":
            ord_new_char = ord("a") + (a * (ord(char) - ord("a")) + b) % 26
        else:
            ord_new_char = ord(char)
        ciphertext += chr(ord_new_char)
    return ciphertext
