DICTIONARY = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DICTIONARY_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt_poly_shift(plaintext, odd_shift, even_shift):

    ciphertext = ""
    for i, element in enumerate(plaintext):
        if element in DICTIONARY or element in DICTIONARY_UPPER:
            shift = even_shift if (i + 1) % 2 == 0 else odd_shift

            if element.isupper():
                indx = DICTIONARY_UPPER.index(element)
                the_val = DICTIONARY_UPPER[(indx + shift) % len(DICTIONARY_UPPER)]
                ciphertext += the_val
            elif element.islower():
                indx = DICTIONARY.index(element)
                the_val = DICTIONARY[(indx + shift) % len(DICTIONARY)]
                ciphertext += the_val
        else:
            ciphertext += element

    return ciphertext
