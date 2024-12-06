def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    if not plaintext:
        return plaintext

    ciphertext = []
    keyword = (keyword.lower() * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for i, letter in enumerate(plaintext):
        shift = ord(keyword[i].lower()) - ord("a")

        if "A" <= letter <= "Z":
            new_letter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            new_letter = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            new_letter = letter

        ciphertext.append(new_letter)

    return "".join(ciphertext)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    if not ciphertext:
        return ciphertext

    plaintext = []
    keyword = (keyword.lower() * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for i, letter in enumerate(ciphertext):
        shift = ord(keyword[i].lower()) - ord("a")

        if "A" <= letter <= "Z":
            new_letter = chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= letter <= "z":
            new_letter = chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            new_letter = letter

        plaintext.append(new_letter)

    return "".join(plaintext)
