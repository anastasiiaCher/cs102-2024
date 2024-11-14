def encrypt_atbash(plaintext: str) -> str:
    """
    encrypt in Atbash
    """
    i = 0
    ciphertext = ""
    for i in range(len(plaintext)):
        sim = ord(plaintext[i])
        if sim < 65 or sim > 90 and sim < 97 or sim > 122:
            ciphertext = ciphertext + chr(sim)
        else:
            if sim <= 90:
                ciphertext = ciphertext + chr(90 - sim + 1 + 64)
            if sim >= 97:
                ciphertext = ciphertext + chr(122 - sim + 1 + 96)
    return ciphertext
