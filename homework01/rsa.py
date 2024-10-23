"""
RSA algorithm
"""

import random
import typing as tp

# python3 -m unittest -v tests.test_rsa


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    flag = 1
    if n < 2:
        return False

    for i in range(2, int(abs(n) ** 0.5 + 1)):
        if abs(n) % i == 0:
            flag = 0
            break
    return bool(flag)


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if a == 0 or b == 0:
        return a + b
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    a_array = []
    b_array = []
    x_array = []
    y_array = []
    a = phi
    b = e
    a_array.append(a)
    b_array.append(b)
    x_array.append(0)
    y_array.append(0)
    while a % b != 0:
        c = b
        b = a % b
        a = c
        a_array.append(a)
        b_array.append(b)
        x_array.append(0)
        y_array.append(0)
    x_array[-1] = 0
    y_array[-1] = 1
    for i in range(len(y_array) - 2, -1, -1):
        x_array[i] = y_array[i + 1]
        y_array[i] = x_array[i + 1] - y_array[i + 1] * (a_array[i] // b_array[i])
        # print(x_array[i], y_array[i])

    return y_array[0] % phi


def generate_keypair(pp: int, qq: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """
    generating rsa
    """
    if not (is_prime(pp) and is_prime(qq)):
        raise ValueError("Both numbers must be prime.")
    if pp == qq:
        raise ValueError("p and q cannot be equal")

    n = pp * qq

    phi = (pp - 1) * (qq - 1)

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
    """
    Encrypting
    :param pk:
    :param plaintext:
    :return:
    """
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """
    Decrypting
    :param pk:
    :param ciphertext:
    :return:
    """
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
