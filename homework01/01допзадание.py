def encrypt_poly_shift(plaintext: str, odd_shift: int, even_shift: int) -> str:
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    alphabet_length = len(alphabet)

    encrypted_text = []

    for index, char in enumerate(plaintext):
        position = index + 1

        if char.lower() in alphabet:
            shift = odd_shift if position % 2 != 0 else even_shift

            original_index = alphabet.index(char.lower())

            new_index = (original_index + shift) % alphabet_length

            encrypted_char = alphabet[new_index]

            if char.isupper():
                encrypted_text.append(encrypted_char.upper())
            else:
                encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

plaintext = input()
odd_shift = int(input())
even_shift = int(input())
encrypted = encrypt_poly_shift(plaintext, odd_shift, even_shift)
print(encrypted)