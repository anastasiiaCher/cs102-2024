def encrypt_scytale(plaintext, n):
    from math import ceil

def encrypt_scytale(plaintext, n):
    from math import ceil
    
    m = ceil(len(plaintext) / n)
    
    while len(plaintext) < n * m:
        plaintext += "*"

    ciphertext = []

    for i in range(n):
        for j in range(m):
            ciphertext.append(plaintext[j * n + i])
    for element in ciphertext:
        if element.isspace():
            ind = ciphertext.index(element)
            ciphertext.pop(ind)
            ciphertext.insert(ind, "_")

    
    return ''.join(ciphertext)

print(encrypt_scytale("НАС АТАКУЮТ", 4))