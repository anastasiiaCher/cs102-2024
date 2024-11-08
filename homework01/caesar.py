def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
<<<<<<< HEAD
            stayInAlphabet = ord(char) + shift
=======
            stayInAlphabet = ord(char) + shift 
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
            if stayInAlphabet > ord("Z"):
                stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                ciphertext += finalLetter
            else:
                ciphertext += chr(stayInAlphabet)
        if char.islower():
<<<<<<< HEAD
            stayInAlphabet = ord(char) + shift
=======
            stayInAlphabet = ord(char) + shift 
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
            if stayInAlphabet > ord("z"):
                stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                ciphertext += finalLetter
            else:
                ciphertext += chr(stayInAlphabet)
        if not char.isalpha():
            ciphertext += char
    return ciphertext
    

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
<<<<<<< HEAD
            stayInAlphabet = ord(char) - shift
=======
            stayInAlphabet = ord(char) - shift 
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
            if stayInAlphabet < ord("A"):
                stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                plaintext += finalLetter
            else:
                plaintext += chr(stayInAlphabet)
        if char.islower():
<<<<<<< HEAD
            stayInAlphabet = ord(char) - shift
=======
            stayInAlphabet = ord(char) - shift 
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
            if stayInAlphabet < ord("a"):
                stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                plaintext += finalLetter
            else:
                plaintext += chr(stayInAlphabet)
        if not char.isalpha():
            plaintext += char
    return plaintext
