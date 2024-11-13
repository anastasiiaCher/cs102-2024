def encrypt_scytale(plaintext, n):
    """
    Tests the encryption to scytale.
    >>> encrypt_scytale("ПИТОН ЛУЧШИЙ", 3)
    'ПОЛШИНУИТ_ЧЙ'
    >>> encrypt_scytale("python is the best", 5)
    'pntey_hstieths_o_b'
    >>> encrypt_scytale("всем привет как дела", 7)
    'виксв_еедмте__лпкара'
    """

    plaintext = plaintext.replace(' ', '_')
    result = [''] * n

    for i in range(len(plaintext)):
        col = i % n
        result[col] += plaintext[i]
    ciphertext = ''.join(result)

    return ciphertext
