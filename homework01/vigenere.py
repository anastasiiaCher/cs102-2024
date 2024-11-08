def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
<<<<<<< HEAD
    repeats = (len(plaintext) // len(keyword) + 1) * keyword
    rez = repeats[: len(plaintext)]
    index = 0
    for i in plaintext:
        if ord("a") > ord(i.lower()) or ord(i.lower()) > ord("z"):
            ciphertext += i
            index += 1
        else:
            k = rez[index]
            shift = ord(k.lower()) - ord("a")
            if ord(i.lower()) + shift <= ord("z"):
                index += 1
                ciphertext += chr(ord(i) + shift)
            else:
                if i.isupper():
                    ciphertext += (chr(ord("a") + (ord(i.lower()) + shift - ord("z")) - 1)).upper()
                if i.islower():
                    ciphertext += (chr(ord("a") + (ord(i) + shift - ord("z")) - 1)).lower()
                index += 1
=======
    for char in range(len(plaintext)):
        if plaintext[char].isupper():
            new_ord = ord(plaintext[char]) + (ord(keyword[char % len(keyword)])-ord("A"))
            if new_ord > ord("Z"):
                new_ord -= 26
            ciphertext += chr(new_ord)
            
        else:
            new_ord = ord(plaintext[char]) + (ord(keyword[char % len(keyword)]) - ord("a"))
            if new_ord > ord("z"):
                new_ord -= 26
            ciphertext += chr(new_ord)
            
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
<<<<<<< HEAD
    repeats = (len(ciphertext) // len(keyword) + 1) * keyword
    rez = repeats[: len(ciphertext)]
    index = 0
    for i in ciphertext:
        if ord("a") > ord(i.lower()) or ord(i.lower()) > ord("z"):
            plaintext += i
            index += 1
        else:
            k = rez[index]
            shift = ord(k.lower()) - ord("a")
            if ord(i.lower()) - shift >= ord("a"):
                index += 1
                plaintext += chr(ord(i) - shift)
            else:
                if i.isupper():
                    plaintext += (chr(ord(i) - ord("a") + ord("z") - shift + 1)).upper()
                if i.islower():
                    plaintext += (chr(ord(i) - ord("a") + ord("z") - shift + 1)).lower()
                index += 1
=======
    
    for char in range(len(ciphertext)):
        if ciphertext[char].isupper():
            new_ord = ord(ciphertext[char]) - (ord(keyword[char % len(keyword)]) - ord("A"))
            if new_ord < ord("A"):
                new_ord += 26
            plaintext += chr(new_ord)
            
        else:
            new_ord = ord(ciphertext[char]) + (ord(keyword[char % len(keyword)]) - ord("a"))
            if new_ord < ord("a"):
                new_ord += 26
            plaintext += chr(new_ord)
            
>>>>>>> a6f5bf7228dd900b0db3679dfa36982ba85e67c3
    return plaintext
