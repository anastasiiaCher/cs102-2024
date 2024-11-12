import string


def encrypt_vigenere(plaintext: str, keyword: str):
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)
    ciphertext = ""
    all_ind = []

    while len(keyword) != len(plaintext):
        if len(keyword) < len(plaintext):
            keyword += keyword
        elif len(keyword) > len(plaintext):
            keyword = keyword[:-1]

    for x in range(len(keyword)):
        if keyword[x] in alphabet_uppercase:
            ind = alphabet_uppercase.index(keyword[x])
            all_ind.append(ind)
        elif keyword[x] in alphabet_lowercase:
            ind = alphabet_lowercase.index(keyword[x])
            all_ind.append(ind)

    for j in range(len(plaintext)):
        if plaintext[j] in alphabet_lowercase:
            ind_plain = alphabet_lowercase.index(plaintext[j])
            shift = all_ind[j]
            new_index = ind_plain + shift
            if new_index < len(alphabet_lowercase):
                new_letter = alphabet_lowercase[new_index]
                ciphertext += new_letter
            else:
                new_index2 = (ind_plain + shift) - len(alphabet_lowercase)
                new_letter = alphabet_lowercase[new_index2]
                ciphertext += new_letter

        elif plaintext[j] in alphabet_uppercase:
            ind_plain = alphabet_uppercase.index(plaintext[j])
            shift = all_ind[j]
            new_index = ind_plain + shift
            if new_index < len(alphabet_uppercase):
                new_letter = alphabet_uppercase[new_index]
                ciphertext += new_letter
            else:
                new_index2 = (ind_plain + shift) - len(alphabet_uppercase)
                new_letter = alphabet_uppercase[new_index2]
                ciphertext += new_letter

        else:
            ciphertext += plaintext[j]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str):
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)
    plaintext = ""
    all_ind = []

    while len(keyword) != len(ciphertext):
        if len(keyword) < len(ciphertext):
            keyword += keyword
        elif len(keyword) > len(ciphertext):
            keyword = keyword[:-1]

    for x in range(len(keyword)):
        if keyword[x] in alphabet_uppercase:
            ind = alphabet_uppercase.index(keyword[x])
            all_ind.append(ind)
        elif keyword[x] in alphabet_lowercase:
            ind = alphabet_lowercase.index(keyword[x])
            all_ind.append(ind)

    for j in range(len(ciphertext)):
        if ciphertext[j] in alphabet_lowercase:
            ind_plain = alphabet_lowercase.index(ciphertext[j])
            shift = all_ind[j]
            new_index = ind_plain - shift
            if new_index >= 0:
                new_letter = alphabet_lowercase[new_index]
                plaintext += new_letter
            else:
                new_index2 = len(alphabet_lowercase) + new_index
                new_letter = alphabet_lowercase[new_index2]
                plaintext += new_letter

        elif ciphertext[j] in alphabet_uppercase:
            ind_plain = alphabet_uppercase.index(ciphertext[j])
            shift = all_ind[j]
            new_index = ind_plain - shift
            if new_index >= 0:
                new_letter = alphabet_uppercase[new_index]
                plaintext += new_letter
            else:
                new_index2 = len(alphabet_uppercase) + new_index
                new_letter = alphabet_uppercase[new_index2]
                plaintext += new_letter

        else:
            plaintext += ciphertext[j]

    return plaintext


print(decrypt_vigenere("tfvzzvwkeaqv lq aqvpzf", "lsci"))
