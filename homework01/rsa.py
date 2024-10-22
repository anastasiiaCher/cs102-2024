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
    # Проверка на числа, которые не являются простыми
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Проверка делимости на 2 и 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Проверка всех чисел от 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Проверяем числа вида 6k ± 1

    return True
    pass

