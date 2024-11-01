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
    for S in plaintext:
        if "A" <= S <= "Z":
            new_S = chr((ord(S) - ord("A") + shift) % 26 + ord("A"))
            ciphertext += new_S
        elif "a" <= S <= "z":
            new_S = chr((ord(S) - ord("a") + shift) % 26 + ord("a"))
            ciphertext += new_S
        else:
            ciphertext += S
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
    for S in ciphertext:
        if "A" <= S <= "Z":
            new_S = chr((ord(S) - ord("A") - shift) % 26 + ord("A"))
            plaintext += new_S
        elif "a" <= S <= "z":
            new_S = chr((ord(S) - ord("a") - shift) % 26 + ord("a"))
            plaintext += new_S
        else:
            plaintext += S
    return plaintext
if __name__ == "__main__":
    print(encrypt_caesar(input()))
    print(decrypt_caesar(input()))