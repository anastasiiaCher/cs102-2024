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
    ciphertext = ""
    keyword = keyword.lower()

    while len(keyword) < len(plaintext):
        keyword += keyword
    if len(keyword) != len(plaintext):
        keyword = keyword[:len(plaintext)]

    for el in keyword:
        keys.append(ord(el))

    for i in range(len(plaintext)):

        if plaintext[i] in " ,-":
            ciphertext += plaintext[i]
            continue

        if plaintext[i].isupper():

            shift = keys[i] - 97
            new_ord = ord(plaintext[i]) + shift

            if new_ord > 90:
                new_ord -= 26

            ciphertext += chr(new_ord)

        else:

            shift = keys[i] - 97
            new_ord = ord(plaintext[i]) + shift

            if new_ord > 122:
                new_ord -= 26

            ciphertext += chr(new_ord)

    return ciphertext


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

    plaintext = ""
    keys = []

    keyword = keyword.lower()

    while len(keyword) < len(ciphertext):
        keyword += keyword

    if len(keyword) != len(ciphertext):
        keyword = keyword[: len(ciphertext)]

    for el in keyword:
        keys.append(ord(el))

    for i in range(len(ciphertext)):

        if ciphertext[i] in " ,-":
            plaintext += ciphertext[i]
            continue

        if ciphertext[i].isupper():

            shift = keys[i] - 97
            new_ord = ord(ciphertext[i]) - shift

            if new_ord < 65:
                new_ord += 26

            plaintext += chr(new_ord)

        else:

            shift = keys[i] - 97
            new_ord = ord(ciphertext[i]) - shift

            if new_ord < 97:
                new_ord += 26

            plaintext += chr(new_ord)
    # PUT YOUR CODE HERE
    return plaintext
