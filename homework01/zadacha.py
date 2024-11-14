def encrypt_transposition(plaintext, block_size, id1, id2):
    if id1 >= block_size or id2 >= block_size:
        raise ValueError("Индексы id1 и id2 должны быть меньше размера блока.")

    blocks = [
        plaintext[i : i + block_size] for i in range(0, len(plaintext), block_size)
    ]
    encrypted_blocks = []

    for block in blocks:
        if len(block) < block_size:
            encrypted_blocks.append(block)
            continue

        block_list = list(block)

        block_list[id1], block_list[id2] = block_list[id2], block_list[id1]

        encrypted_blocks.append("".join(block_list))

    return "".join(encrypted_blocks)


if __name__ == "__main__":
    plaintext = "abcdefghij"
    block_size = 4
    id1 = 1
    id2 = 3
    encrypted_text = encrypt_transposition(plaintext, block_size, id1, id2)
    print(encrypted_text)
