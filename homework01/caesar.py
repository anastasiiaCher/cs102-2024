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
    up_alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_alph_eng = "abcdefghijklmnopqrstuvwxyz"

    for el in plaintext:
        if el in up_alph_eng:
            ord_letter = up_alph_eng.index(el) + shift
            if ord_letter > 26:
                ord_letter -= 26
            ciphertext += up_alph_eng[ord_letter]

        elif el in low_alph_eng:
            ord_letter = low_alph_eng.index(el) + shift
            while ord_letter > 26:
                ord_letter -= 26
            ciphertext += low_alph_eng[ord_letter]
        else:
            ciphertext += el
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
    up_alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_alph_eng = "abcdefghijklmnopqrstuvwxyz"

    for el in ciphertext:
        if el in up_alph_eng:
            ord_letter = up_alph_eng.index(el) - shift
            while ord_letter < 0:
                ord_letter += 26
            plaintext += up_alph_eng[ord_letter]

        elif el in low_alph_eng:
            ord_letter = low_alph_eng.index(el) - shift
            while ord_letter < 0:
                ord_letter += 26
            plaintext += low_alph_eng[ord_letter]

        else:
            plaintext += el
    return plaintext
