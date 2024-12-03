def encrypt_growing_shift(plaintext, start, delta):
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet_len = len(alphabet)
    encrypted_text = ""
    shift = start

    for char in plaintext.upper():
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % alphabet_len
            encrypted_text += alphabet[new_index]
            shift += delta
        else:
            encrypted_text += char

    return encrypted_text
