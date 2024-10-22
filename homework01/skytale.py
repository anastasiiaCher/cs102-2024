def decrypt_skytale(plaintext, n):
    """
    Decrypts a ciphertext using a Skytale cipher.
    >>> decrypt_skytale("A    LWTEWLEHNE'LADLSLTSL", 5)
    "ALL'S WELL THAT ENDS WELL"
    >>> decrypt_skytale("ACDTKATAWATN", 4)
    'ATTACKATDAWN'
    >>> decrypt_skytale("РНОАЫЙКЕСЕ_КТВА", 5)
    'РАКЕТНЫЕ ВОЙСКА'
    """
    table = []
    text = plaintext.replace("_", " ")

    m = len(plaintext) // n
    r = len(text) % m

    for col in range(n):
        if col < r:
            table.append(text[: m + 1])
            text = text[m + 1 :]
        else:
            table.append(text[:m] + " ")
            text = text[m:]

    dec_text = ""
    for i in range(m + 1):
        for j in table:
            a = j[i]
            dec_text += a

    return dec_text.strip()
