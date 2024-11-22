"""Writing a function for new cipher method"""
def encrypt_transposition(plaintext, block_size, id1, id2):
    """Making it a reality"""
    newtext = ""
    if len(plaintext) % block_size == 0:
        pltxt= ""
    else:
        pltxt = plaintext[plaintext - plaintext % block_size + 1 :]
        plaintext = plaintext[: len(plaintext) - len(plaintext) % block_size]
    for i in range(0, len(plaintext), block_size):
        newblock = ""
        newblock += plaintext[i : i + block_size]
        newblock = newblock[:id1] + newblock[id2] + newblock[id1 + 1 : id2] + newblock[id1] + newblock[id2 + 1 :]
        newtext += newblock
    newtext += pltxt
    return newtext


# print(encrypt_transposition('abcdefghij', 2, 0, 1))
