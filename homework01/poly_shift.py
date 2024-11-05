def decrypt_poly_shift(ciphertext, odd_shift, even_shift):
    plaintext = ""
    for i in ciphertext:
        if ord("а") > ord(i.lower()) or ord(i.lower()) > ord("я"):
            plaintext += i
        if ord(i.lower()) % 2 == 0:
            if ord(i.lower()) - odd_shift >= ord("а"):
                if i.isupper():
                    plaintext += (chr(ord(i) - odd_shift)).upper()
                if i.islower():
                    plaintext += (chr(ord(i) - odd_shift)).lower()
            else:
                if i.isupper():
                    plaintext += (chr(ord(i) - ord("а") + ord("я") - odd_shift + 1)).upper()
                if i.islower():
                    plaintext += (chr(ord(i) - ord("а") + ord("я") - odd_shift + 1)).lower()
        else:
            if ord(i.lower()) - even_shift >= ord("а"):
                if i.isupper():
                    plaintext += (chr(ord(i) - even_shift)).upper()
                if i.islower():
                    plaintext += (chr(ord(i) - even_shift)).lower()
            else:
                if i.isupper():
                    plaintext += (chr(ord(i) - ord("а") + ord("я") - even_shift + 1)).upper()
                if i.islower():
                    plaintext += (chr(ord(i) - ord("а") + ord("я") - even_shift + 1)).lower()
    return plaintext
