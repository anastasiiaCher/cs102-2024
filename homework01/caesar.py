import string


def encrypt_caesar(plaintext: str, shift: int):
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet_lowercase:
            ind1 = alphabet_lowercase.index(plaintext[i])
            if int(ind1) + int(shift) < len(alphabet_lowercase):
                new_ind1 = int(ind1) + int(shift)
                new_letter = str(alphabet_lowercase[new_ind1])
                ciphertext += new_letter
            else:
                newind1 = (ind1 + shift) - len(alphabet_lowercase)
                new_letter = str(alphabet_lowercase[newind1])
                ciphertext += new_letter

        elif plaintext[i] in alphabet_uppercase:
            ind2 = alphabet_uppercase.index(plaintext[i])
            if int(ind2) + int(shift) < len(alphabet_uppercase):
                new_ind2 = int(ind2) + int(shift)
                new_letter = str(alphabet_uppercase[new_ind2])
                ciphertext += new_letter
            else:
                newind2 = (ind2 + shift) - len(alphabet_uppercase)
                new_letter = str(alphabet_uppercase[newind2])
                ciphertext += new_letter
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int):
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet_lowercase:
            ind1 = alphabet_lowercase.index(ciphertext[i])
            if int(ind1) - int(shift) >= 0:
                new_ind1 = int(ind1) - int(shift)
                new_letter = str(alphabet_lowercase[new_ind1])
                plaintext += new_letter
            else:
                newind1 = len(alphabet_lowercase) + (ind1 - shift)
                new_letter = str(alphabet_lowercase[newind1])
                plaintext += new_letter

        elif ciphertext[i] in alphabet_uppercase:
            ind2 = alphabet_uppercase.index(ciphertext[i])
            if int(ind2) - int(shift) >= 0:
                new_ind2 = int(ind2) - int(shift)
                new_letter = str(alphabet_uppercase[new_ind2])
                plaintext += new_letter
            else:
                newind2 = len(alphabet_uppercase) + (ind2 - shift)
                new_letter = str(alphabet_uppercase[newind2])
                plaintext += new_letter
        else:
            plaintext += ciphertext[i]

    return plaintext

