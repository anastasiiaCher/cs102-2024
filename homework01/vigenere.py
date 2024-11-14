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
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():  # Check if character is alphabetic
            shift = ord(k.upper()) - ord('A')  # Calculate the shift from the keyword
            new_char = chr((ord(p.upper()) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += new_char
        else:
            ciphertext += p  # Non-alphabetic characters are added unchanged
            
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
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():  # Check if character is alphabetic
            shift = ord(k.upper()) - ord('A')  # Calculate the shift from the keyword
            new_char = chr((ord(c.upper()) - ord('A') - shift) % 26 + ord('A'))
            plaintext += new_char
        else:
            plaintext += c  # Non-alphabetic characters are added unchanged
    return plaintext
