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
        if char.isalpha():
            char_code = ord(char) + shift
            if char.islower():
                if char_code > ord("z"):
                    char_code -= 26
            elif char.isupper():
                if char_code > ord("Z"):
                    char_code -= 26
            ciphertext += chr(char_code)
        else:
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
        if char.isalpha():
            char_code = ord(char) - shift
            if char.islower():
                if char_code < ord("a"):
                    char_code += 26
            elif char.isupper():
                if char_code < ord("A"):
                    char_code += 26
            plaintext += chr(char_code)
        else:
            plaintext += char
    return plaintext
