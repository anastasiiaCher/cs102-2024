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
    keyword = keyword * ((len(plaintext) // len(keyword)) + 1)
    pos_in_keyword = -1
    for i in plaintext:
        pos_in_keyword += 1
        if i.isalpha() is False:
            ciphertext += i
            continue
        if i.isupper() is True:
            shift = (ord(keyword[pos_in_keyword]) - 65) % 26
            if (ord(i) + shift) > 90:
                # print(chr((ord(i) + shift) % 90 + 64))
                ciphertext += chr((ord(i) + shift) % 90 + 64)
            else:
                # print(chr((ord(i) + shift) % 90), i, ord(i) + shift)
                ciphertext += chr(ord(i) + shift)
        else:
            shift = (ord(keyword[pos_in_keyword]) - 97) % 26
            if (ord(i) + shift) > 122:
                ciphertext += chr((ord(i) + shift) % 122 + 96)
            else:
                ciphertext += chr(ord(i) + shift)
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
    keyword = keyword * ((len(ciphertext) // len(keyword)) + 1)
    pos_in_keyword = -1
    for i in ciphertext:
        pos_in_keyword += 1
        if i.isalpha() is False:
            plaintext += i
            continue
        if i.isupper() is True:
            shift = (ord(keyword[pos_in_keyword]) - 65) % 26
            if (ord(i) - shift) < 65:
                # print(chr(90 - (shift - ord(i) + 64)))
                plaintext += chr(90 - (shift - ord(i) + 64))
            else:
                # print(chr(ord(i) - shift), i, ord(i) + shift)
                plaintext += chr(ord(i) - shift)
        else:
            shift = (ord(keyword[pos_in_keyword]) - 97) % 26
            if (ord(i) - shift) < 97:
                plaintext += chr(122 - (shift - ord(i) + 96))
            else:
                # print(chr((ord(i) + shift) % 90), i, ord(i) + shift)
                plaintext += chr(ord(i) - shift)
    return plaintext

#print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))