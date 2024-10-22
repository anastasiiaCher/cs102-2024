def decrypt_skytale(plaintext, n):
    div_text = []
    text = plaintext

    m = (len(plaintext) // n)
    print(len(plaintext), m)

    r = len(text) % m

    for k in range(r):
        div_text.append(text[:m + 1])
        text = text[m + 1:]
    for d in range(r, n):
        div_text.append(text[:m] + "_")
        text = text[m:]

    dec_text = ""
    for i in range(m + 1):
        for j in div_text:
            a = j[i]
            if ord("А") <= ord(a) <= ord("Я") or ord("A") <= ord(a) <= ord("Z") or ord("a") <= ord(a) <= ord(
                    "z") or ord("а") <= ord(a) <= ord("я") or ord(a) == ord("Ё") or ord(a) == ord("ё"):
                dec_text += a
            elif ord(a) == ord("_") or ord(a) == ord(" "):
                dec_text += " "
            else:
                dec_text += a

    return dec_text.strip()
