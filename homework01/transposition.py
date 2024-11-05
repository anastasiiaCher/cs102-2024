"""Разделить текст на равные блоки по n.
Поменять местами буквы, стоящие на указанных позициях, например, вторую с четвертой, первую с третьей или любую другую комбинацию.
Напишите функцию encrypt_transposition(plaintext, block_size, id1, id2) для шифрования текста, где id1 и id2 - индексы 
букв в блоке, которые надо поменять местами, block_size - размер блока. Учитывайте, что индексы букв не могут быть больше 
размера блока.
"""


def encrypt_transposition(plaintext: str, block_size: int, id1: int, id2: int) -> str:
    if id1 >= block_size or id2 >= block_size:
        raise ValueError("Индексы букв не могут быть больше размера блока.")
    blocks = [plaintext[i : i + block_size] for i in range(0, len(plaintext), block_size)]
    encrypted_blocks = []
    for block in blocks:
        if len(block) < block_size:
            encrypted_blocks.append(block)
        else:
            blockl = list(block)
            blockl[id1], blockl[id2] = blockl[id2], blockl[id1]
            encrypted_blocks.append("".join(blockl))

    encrypted_text = "".join(encrypted_blocks)
    return encrypted_text
print(encrypt_transposition("hello", 3, 0, 1))