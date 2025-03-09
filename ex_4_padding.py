def compute_pad(message: str) -> str:
    block_size_bytes = 16
    block_size_bites = block_size_bytes * 8

    message_length = len(message)
    message_length_bin = bin(message_length % 2 ** 8)[2:].rjust(8, "0")

    unchanged_blocks = message_length // block_size_bytes
    last_block = message[unchanged_blocks * block_size_bytes:]
    # <data>  1 <optional 0> 8 bit length
    if len(last_block) * 8 > (block_size_bytes * 8) - 8 - 1:
        zeroes = block_size_bites - 8 - 1 + (block_size_bites - len(last_block) * 8)
    else:
        zeroes = (block_size_bites - 8 - 1 - len(last_block) * 8)
    return f"1{'0' * zeroes}{message_length_bin}"


def main() -> None:
    # Tests for student side debugging only
    assert compute_pad("A" * 14) == "1000000000001110"
    assert compute_pad("A" * 15) == "1000000000000000000000000000000000000000000000000000000000000000" \
                                    "000000000000000000000000000000000000000000000000000000000000000000001111"
    assert compute_pad("A" * 16) == "1000000000000000000000000000000000000000000000000000000000000000" \
                                    "0000000000000000000000000000000000000000000000000000000000010000"
    assert compute_pad("A" * 300) == "10000000000000000000000000101100"


if __name__ == '__main__':
    main()
