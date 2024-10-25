def encrypt_affine(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if "A" <= char <= "Z":
            ord_new_char = ord("A") + (a*(ord(char) - ord("A")) + b) % 26
        elif "a" <= char <= "z":
            ord_new_char = ord("a") + (a*(ord(char) - ord("a")) + b) % 26
        else:
            ord_new_char = ord(char)
        ciphertext += chr(ord_new_char)
    return ciphertext
