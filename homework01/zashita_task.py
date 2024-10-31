"""
This module contains a function to decrypt encrypted Scytale cipher.
"""


def decrypt_scytale(ciphertext, n):
    """
    Decrypts a text encrypted with the Scytale cipher.

    Parameters:
    ciphertext (str): The encrypted text.
    n (int): The width of the original table.

    Returns:
    str: The decrypted message.
    """

    rows = len(ciphertext) // n
    columns = []

    for i in range(n):
        columns_text = ""
        for j in range(rows):
            index = i * rows + j
            columns_text += ciphertext[index]
        columns.append(columns_text)

    decrypted_text = ""
    for j in range(rows):
        for i in range(n):
            decrypted_text += columns[i][j]

    return decrypted_text
