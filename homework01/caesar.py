"""
Caesar cipher and decipher algorithms.
"""


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
    if plaintext == "" or shift == 0:
        return plaintext

    ciphertext = ""
    for letter in plaintext:
        oldcode = ord(letter)
        newcode = oldcode + (shift % 27)

        if "A" <= letter <= "Z":
            letter = chr(newcode % 91 + 65) if newcode > 90 else chr(newcode)
        elif "a" <= letter <= "z":
            letter = chr(newcode % 123 + 97) if newcode > 122 else chr(newcode)

        ciphertext += letter

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
    if ciphertext == "" or shift == 0:
        return ciphertext

    for letter in ciphertext:
        newcode = ord(letter)
        oldcode = newcode - (shift % 27)

        if "A" <= letter <= "Z":
            letter = chr(oldcode + 26) if oldcode < 65 else chr(oldcode)
        elif "a" <= letter <= "z":
            letter = chr(oldcode + 26) if oldcode < 97 else chr(oldcode)

        plaintext += letter

    return plaintext
