def encrypt_atbash(plaintext):
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                if ord(i) <= ord("е"):
                    ciphertext += chr(ord("я") - ord(i) + ord("а"))
                elif i == "ё":
                    ciphertext += "щ"
                elif i == "ж":
                    ciphertext += "ш"
                elif i == "щ":
                    ciphertext += "ё"
                elif ord("е") + 1 < ord(i) < ord("щ"):
                    ciphertext += chr(ord("я") - ord(i) + ord("а") - 1)
                else:
                    ciphertext += chr(ord("я") - ord(i) + ord("а"))
            else:
                if ord(i) <= ord("Е"):
                    ciphertext += chr(ord("Я") - ord(i) + ord("А"))
                elif i == "Ё":
                    ciphertext += "Щ"
                elif i == "Ж":
                    ciphertext += "Ш"
                elif i == "Щ":
                    ciphertext += "Ё"
                elif ord("Е") + 1 < ord(i) < ord("Щ"):
                    ciphertext += chr(ord("Я") - ord(i) + ord("А") - 1)
                else:
                    ciphertext += chr(ord("Я") - ord(i) + ord("А"))
        else:
            ciphertext += i
    return ciphertext


