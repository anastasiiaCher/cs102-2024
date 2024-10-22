def encrypt_atbash(plaintext: str):
    ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha():
            gap = ord(symbol) - ord("a" if symbol.islower() else "A") 
            ciphertext += chr(ord("z" if symbol.islower() else "Z") - gap)
        else:
            ciphertext += symbol

    return ciphertext

print(encrypt_atbash("aA zZ bB yY"))