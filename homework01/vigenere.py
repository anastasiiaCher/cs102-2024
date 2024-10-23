"""Реализация шифра Виженера"""


def encrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    keyword = keyword.lower()

    result = ""
    shift_base = ord("a")
    for index in range(len(ciphertext)):
        char = ciphertext[index]

        if char.isalpha():
            key_index = index % len(keyword)

            key = ord(keyword[key_index]) - shift_base
            shift = ord(char) + key

            is_lower = char.islower() and shift > ord("z")
            is_upper = char.isupper() and shift > ord("Z")

            if is_lower or is_upper:
                shift -= 26  # ща

            result += chr(shift)
        else:
            result += char

    return result


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

    keyword = keyword.lower()

    result = ""
    shift_base = ord("a")
    for index in range(len(ciphertext)):
        char = ciphertext[index]

        if char.isalpha():
            key_index = index % len(keyword)

            key = ord(keyword[key_index]) - shift_base
            shift = ord(char) - key

            is_lower = char.islower() and shift < shift_base
            is_upper = char.isupper() and shift < ord("A")

            if is_lower or is_upper:
                shift += 26

            result += chr(shift)
        else:
            result += char

    return result


# result = decrypt_vigenere('tfvzzvwkeaqv lq aqvpzf', 'lsci')
# print(result)
