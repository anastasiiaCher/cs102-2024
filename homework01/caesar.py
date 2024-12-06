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
         if "A" <= char <= "Z":
             if ord(char) + shift > ord("Z"):
                 new_char = chr(ord(char) + shift - 26)
             else:
                 new_char = chr(ord(char) + shift)
         elif "a" <= char <= "z":
             if ord(char) + shift > ord("z"):
                 new_char = chr(ord(char) + shift - 26)
             else:
                 new_char = chr(ord(char) + shift)
         else:
             new_char = char
         ciphertext += new_char
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
         if "A" <= char <= "Z":
             if ord(char) - shift < ord("A"):
                 new_char = chr(ord(char) - shift + 26)
             else:
                 new_char = chr(ord(char) - shift)
         elif "a" <= char <= "z":
             if ord(char) - shift < ord("a"):
                 new_char = chr(ord(char) - shift + 26)
             else:
                 new_char = chr(ord(char) - shift)
         else:
             new_char = char
         plaintext += new_char
    return plaintext
    