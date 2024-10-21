"""модуль кодирования и декодирования по шифру"""
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    list_of_ceaser = []
    list_of_plaintext = []
    letter_2 = ""

    for i in range(len(plaintext)):
        list_of_plaintext.append(plaintext[i : i + 1])   
        letter = plaintext[i : i + 1]
        o_var = ord(letter)
        if o_var in range(31,65) or o_var in range(91,97):
            letter_2 = chr(o_var)
        elif o_var in range(65,88) or  o_var in range(97,120):
            letter_2 = chr(o_var + shift)
        elif  o_var in range(120,123) or o_var in range(88,91):
            letter_2 = chr(o_var - 23)
        list_of_ceaser.append(letter_2)
    for d in range(len(plaintext)):
        ciphertext += list_of_ceaser[d]
    return ciphertext


print("введите что-то")
print(encrypt_caesar(input()))


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    list_of_ceaser = []
    list_of_ciphertext = []
    letter_2 = ""
    for i in range(len(ciphertext)):
        list_of_ciphertext.append(ciphertext[i : i + 1])
        letter = ciphertext[i : i + 1]
        o_var = ord(letter)
        if o_var in range(31,65) or  o_var in range(91,97):
            letter_2 = chr(o_var)
        elif o_var in range(68,91) or o_var in range(100,123):
            letter_2 = chr(o_var - shift)
        elif o_var in range(97,100) or o_var in range(65,68):
            letter_2 = chr(o_var + 23)
        list_of_ceaser.append(str(letter_2))
    for d in range(len(ciphertext)):
        plaintext += list_of_ceaser[d]
    return plaintext


print(decrypt_caesar(input()))
