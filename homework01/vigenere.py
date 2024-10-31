"""
Vigenere encrypt and decrypt algorithms.
"""
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
    keyword = keyword * (len(plaintext) // (len(keyword)) + 1)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if plaintext == "":
        return plaintext

    for i, letter in enumerate(plaintext):
        shift = alphabet.index(keyword[i])
        letter = plaintext[i]
        oldcode = ord(letter)
        newcode = oldcode + (shift % 27)

        if 65 <= oldcode <= 90:
            letter = chr(newcode % 91 + 65) if newcode > 90 else chr(newcode)
        elif 97 <= oldcode <= 122:
            letter = chr(newcode % 123 + 97) if newcode > 122 else chr(newcode)

        ciphertext += letter

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
    keyword = keyword.lower()
    keyword = keyword * (len(ciphertext) // (len(keyword)) + 1)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if ciphertext == "":
        return ciphertext

    for i, letter in enumerate(ciphertext):
        shift = alphabet.index(keyword[i])
        letter = ciphertext[i]
        newcode = ord(letter)
        oldcode = newcode - (shift % 27)

        if 65 <= newcode <= 90:
            letter = chr(oldcode + 26) if oldcode < 65 else chr(oldcode)
        elif 97 <= newcode <= 122:
            letter = chr(oldcode + 26) if oldcode < 97 else chr(oldcode)

        plaintext += letter

    return plaintext
