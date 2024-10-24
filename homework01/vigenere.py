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
    for char in range(len(plaintext)):
        if plaintext[char].isupper():
            new_ord = ord(plaintext[char]) + (ord(keyword[char % len(keyword)])-ord("A"))
            if new_ord > ord("Z"):
                new_ord -= 26
            ciphertext += chr(new_ord)
            
        else:
            new_ord = ord(plaintext[char]) + (ord(keyword[char % len(keyword)]) - ord("a"))
            if new_ord > ord("z"):
                new_ord -= 26
            ciphertext += chr(new_ord)
            
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
    
    for char in range(len(ciphertext)):
        if ciphertext[char].isupper():
            new_ord = ord(ciphertext[char]) - (ord(keyword[char % len(keyword)]) - ord("A"))
            if new_ord < ord("A"):
                new_ord += 26
            plaintext += chr(new_ord)
            
        else:
            new_ord = ord(ciphertext[char]) + (ord(keyword[char % len(keyword)]) - ord("a"))
            if new_ord < ord("a"):
                new_ord += 26
            plaintext += chr(new_ord)
            
    return plaintext
