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

    while shift >= 26:
        shift -= 26

    for el in plaintext:

        if el.isalpha():
            ord_letter = ord(el)

            if 65 <= ord_letter <= 90:
                ord_letter += shift

                if ord_letter > 90:
                    ord_letter -= 26

            else:
                ord_letter += shift

                if ord_letter > 122:
                    ord_letter -= 26

            ciphertext += chr(ord_letter)

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

    while shift >= 26:
        shift -= 26

    for el in ciphertext:

        if el.isalpha():
            ord_letter = ord(el)

            if 65 <= ord_letter <= 90:
                ord_letter -= shift

                if ord_letter < 65:
                    ord_letter += 26

            else:
                ord_letter -= shift

                if ord_letter < 97:
                    ord_letter += 26

            plaintext += chr(ord_letter)

        else:
            plaintext += el

    return plaintext
