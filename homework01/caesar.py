def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """Encrypting with Caesar cipher"""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext

texts = ["PYTHON", "python", "Python3.6", ""]
shift = 3

for text in texts:
    encrypted_text = encrypt_caesar(text, shift)
    print(f"Исходный текст: {text}")
    print(f"Зашифрованный текст: {encrypted_text}")
    print("-" * 20)

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
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
        else:
            shifted_char = char
        plaintext += shifted_char
    return plaintext

    texts = ["SBWKRQ", "sbwkrq", "Sbwkrq3.6", ""]
    shift = 3

    for text in texts:
        decrypted_text = decrypt_caesar(text, shift)
        print(f"Зашифрованный текст: {text}")
        print(f"Дешифрованный текст: {decrypted_text}")
        print("-" * 20)
    return plaintext
