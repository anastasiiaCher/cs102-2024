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
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                the_val = chr(ord(i) + shift)
                if ord(the_val) > ord("Z"):
                    ciphertext += chr((ord("A")) + ((ord(the_val) - ord("Z")) - 1))
                else:
                    ciphertext += the_val

            elif i.islower():
                the_val = chr(ord(i) + shift)
                if ord(the_val) > ord("z"):
                    ciphertext += chr((ord("a")) + ((ord(the_val) - ord("z")) - 1))
                else:
                    ciphertext += the_val
        else:
            ciphertext += i
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


    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for i in ciphertext:
        if i.isalpha():
            new_letter_id = None
            is_upper = i.isupper()
            for letter in alphabet:
                if letter == i.lower():
                    letter_id = alphabet.index(letter)
                    new_letter_id = letter_id - shift if letter_id - shift <= 0 else letter_id - shift - len(alphabet)
            plaintext += alphabet[new_letter_id].upper() if is_upper else alphabet[new_letter_id]
        else:
            plaintext += i

    return plaintext
