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
    if not plaintext or shift == 0:
        return plaintext

    ciphertext = ""
    for letter in plaintext:
        if "A" <= letter <= "Z":
            new_letter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            new_letter = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            new_letter = letter
        ciphertext += new_letter

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
    if not ciphertext or shift == 0:
        return ciphertext

    plaintext = ""
    for letter in ciphertext:
        if "A" <= letter <= "Z":
            new_letter = chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            new_letter = chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            new_letter = letter
        plaintext += new_letter

    return plaintext
