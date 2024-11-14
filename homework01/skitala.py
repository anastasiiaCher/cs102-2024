def encrypt_scytale(plaintext, n):

    plaintext = plaintext.replace(" ", "_")
    result = [""] * n

    for i in range(len(plaintext)):
        col = i % n
        result[col] += plaintext[i]
        ciphertext = "".join(result)

    return ciphertext
