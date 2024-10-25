def encrypt_affine(plaintext, a, b, language):
    """Affine encrypt function for English, Russian"""

    ciphertext = ""
    ord_letter = 0

    up_alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_alph_eng = "abcdefghijklmnopqrstuvwxyz"
    up_alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    low_alph_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if language == 'English':
        m = 26
        for let in plaintext:
            if let in " ,.-":
                ciphertext += let
                continue
            if let in up_alph_eng:
                ord_letter = up_alph_eng.index(let)
                let = (a * ord_letter + b) % m
                ciphertext += up_alph_eng[let]
            else:
                ord_letter = low_alph_eng.index(let)
                let = (a * ord_letter + b) % m
                ciphertext += low_alph_eng[let]
    elif language == "Russian":
        m = 33
        for let in plaintext:
            if let in " ,.-":
                ciphertext += let
                continue

            if let in up_alph_rus:
                ord_letter = up_alph_rus.index(let)
                let = (a * ord_letter + b) % m
                ciphertext += up_alph_rus[let]
            else:
                ord_letter = low_alph_rus.index(let)
                let = (a * ord_letter + b) % m
                ciphertext += low_alph_rus[let]
    else:
        return "Language is not defined"

    return ciphertext
