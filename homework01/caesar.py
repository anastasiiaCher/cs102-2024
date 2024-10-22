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
    for alpha in plaintext:
        if "A" <= alpha <= "Z":
            ciphertext += chr(ord("A") + ((ord(alpha) + shift - ord("A")) % 26))
        elif "a" <= alpha <= "z":
            ciphertext += chr(ord("a") + ((ord(alpha) + shift - ord("a")) % 26))
        else:
            ciphertext += alpha

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
    for alpha in ciphertext:
        if "A" <= alpha <= "Z":
            plaintext += chr(ord("Z") - ((ord("Z") - ord(alpha) + shift) % 26))
        elif "a" <= alpha <= "z":
            plaintext += chr(ord("z") - ((ord("z") - ord(alpha) + shift) % 26))
        else:
            plaintext += alpha

    return plaintext
