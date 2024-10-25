def encrypt_affine(plaintext, a, b):
    """affine encrypt function for English"""

    ciphertext = ""
    m, ord_letter = 26, 0

    up_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_alph = "abcdefghijklmnopqrstuvwxyz"

    for let in plaintext:

        if let in " ,.-":
            ciphertext += let
            continue

        if let in up_alph:
            ord_letter = up_alph.index(let)
            let = (a * ord_letter + b) % m
            ciphertext += up_alph[let]
        else:
            ord_letter = low_alph.index(let)
            let = (a * ord_letter + b) % m
            ciphertext += low_alph[let]

    return ciphertext
