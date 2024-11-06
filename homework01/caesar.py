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

    for ch in plaintext:
        old_int = ord(ch)
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
            new_char = ch

        ciphertext = ciphertext + new_char

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
    
    for ch in ciphertext:
        old_int = ord(ch)
        overflow = 0
        
        if( 96 < old_int < 123):
            if old_int - shift < 97:
                overflow = 26
            new_char = chr(old_int - shift + overflow)
        elif( 64 < old_int < 91):
            if old_int - shift < 65:
                overflow = 26
            new_char = chr(old_int - shift + overflow)
        else:
            new_char = ch

        plaintext = plaintext + new_char


    return plaintext