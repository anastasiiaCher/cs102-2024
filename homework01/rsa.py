import random
import typing as tp


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
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b:
        a, b = b, a % b
    return abs(a)


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    old_r, r = phi, e
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_t < 0:
        old_t += phi

    return old_t


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """
    Generate public and private keypairs using the RSA algorithm.
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    return (e, n), (d, n)


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """
    Encrypt the plaintext using the public or private key.
    """
    key, n = pk
    return [(ord(char) ** key) % n for char in plaintext]


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """
    Decrypt the ciphertext using the public or private key.
    """
    key, n = pk
    return "".join(chr((char**key) % n) for char in ciphertext)


if __name__ == "__main__":
    print("RSA Encrypter/Decrypter")
    try:
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        q = int(input("Enter another prime number (not the same as above): "))
        print("Generating your public/private keypairs now . . .")
        public, private = generate_keypair(p, q)
        print("Your public key is ", public, " and your private key is ", private)
        message = input("Enter a message to encrypt with your private key: ")
        encrypted_msg = encrypt(private, message)
        print("Your encrypted message is: ")
        print(" ".join(map(str, encrypted_msg)))
        print("Decrypting message with public key ", public, " . . .")
        print("Your message is:")
        print(decrypt(public, encrypted_msg))
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
