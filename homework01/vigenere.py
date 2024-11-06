def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    int_key = []

    for index, char in enumerate(keyword):
        if (96 < ord(char) < 123):
            int_key.append(ord(char) - 97)
        elif(64 < ord(char) < 91):
            int_key.append(ord(char) - 65)

    for index, char in enumerate(plaintext):
        shift = int_key[index % len(int_key)]
        old_int = ord(char)
        overflow = 0
        
        if( 96 < old_int < 123):
            if old_int + shift > 122:
                overflow = -26
            new_char = chr(old_int + shift + overflow)
        elif( 64 < old_int < 91):
            if old_int + shift > 90:
                overflow = -26
            new_char = chr(old_int + shift + overflow)
        else:
            new_char = char

        ciphertext = ciphertext + new_char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext