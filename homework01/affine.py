"""
Encrypting and decrypting an Affine cipher
"""

def encrypt_affine(plaintext: str, shift: int = 3, a: int = 1) -> str:
    """
    Encrypts plaintext using an Affine cipher.
    >>> encrypt_affineencrypt_affine("Аффина", 4, 1)
    Дшшмсд
    """
    ciphertext = ""
    m = 33
    for i in plaintext:
        if ord('А') > ord(i) or ord(i) > ord('я'):
            ciphertext += i
            continue
        if ord('а') <= ord(i) <= ord('я'):
            ciphertext += chr((a * (ord(i) - ord('а')) + shift) % m + ord('а'))
        else:
            ciphertext += chr((a * (ord(i) - ord('А')) + shift) % m + ord('А'))

    return ciphertext
