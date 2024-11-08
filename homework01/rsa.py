"""RSA Cipher Machine"""

import random
import typing as tp


def is_prime(n: int) -> bool:
    """Checking if the number is prime"""
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def gcd(a: int, b: int) -> int:
    """Euclid's algorithm for determining the greatest common divisor."""
    if a != 0 and b != 0:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    return max(a, b)


def multiplicative_inverse(e: int, phi: int) -> int:
    """Euclid's extended algorithm for finding the multiplicative inverse of two numbers."""
    a = e
    b = phi
    if phi > e:
        a, b = phi, e
    l_a = [a]
    l_b = [b]
    while a % b > 0:
        a, b = b, a % b
        l_b.append(b)
        l_a.append(a)
    l_x = [0]
    l_y = [1]
    for i in range(len(l_a) - 1):
        l_x.append(l_y[i])
        l_y.append(l_x[i] - (l_y[i] * (l_a[-i - 2] // l_b[-i - 2])))
    return l_y[-1] % phi


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """Generating keypairs"""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char**key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
