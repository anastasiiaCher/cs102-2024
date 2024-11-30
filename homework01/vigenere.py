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

    if len(plaintext) > len(keyword):
        diff = len(plaintext) - len(keyword)
        for i in range(diff):
            keyword += keyword[i]
    nums = []
    ciphertext = ""

    for i in range(len(keyword)):
        if keyword[i].isalpha():
            if keyword[i].islower():
                nums.append((ord(keyword[i]) - ord("a")) % 26)
            else:
                nums.append((ord(keyword[i]) - ord("A")) % 26)
        else:
            nums.append(0)

    for i in range(len(nums)):
        if plaintext[i].isalpha():
            if plaintext[i].islower():
                if ord(plaintext[i]) + nums[i] <= ord("z"):
                    ciphertext += chr(ord(plaintext[i]) + nums[i])
                else:
                    ciphertext += chr(ord(plaintext[i]) + nums[i] - 26)
            else:
                if ord(plaintext[i]) + nums[i] <= ord("Z"):
                    ciphertext += chr(ord(plaintext[i]) + nums[i])
                else:
                    ciphertext += chr(ord(plaintext[i]) + nums[i] - 26)
        else:
            ciphertext += plaintext[i]
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

    if len(ciphertext) > len(keyword):
        diff = len(ciphertext) - len(keyword)
        for i in range(diff):
            keyword += keyword[i]
    nums = []
    plaintext = ""
    for i in range(len(ciphertext)):
        if keyword[i].isalpha():
            if keyword[i].islower():
                nums.append((ord(keyword[i]) - ord("a")) % 26)
            else:
                nums.append((ord(keyword[i]) - ord("A")) % 26)
        else:
            nums.append(0)

    for i in range(len(nums)):
        if ciphertext[i].isalpha():
            if ciphertext[i].islower():
                if ord(ciphertext[i]) - nums[i] >= ord("a"):
                    plaintext += chr(ord(ciphertext[i]) - nums[i])
                else:
                    plaintext += chr(ord(ciphertext[i]) - nums[i] + 26)
            else:
                if ord(ciphertext[i]) - nums[i] >= ord("A"):
                    plaintext += chr(ord(ciphertext[i]) - nums[i])
                else:
                    plaintext += chr(ord(ciphertext[i]) - nums[i] + 26)
        else:
            plaintext += ciphertext[i]
    return plaintext
