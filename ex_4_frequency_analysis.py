import string
from collections import defaultdict


def frequency_analysis(filepath: str) -> dict[str, int]:
    alphabet_frequency_init = dict.fromkeys(string.ascii_lowercase, 0)
    frequency_dict = defaultdict(int, alphabet_frequency_init)
    with open(filepath) as fh:
        contents = fh.read().lower()
        for letter in contents:
            if letter in string.ascii_lowercase:
                frequency_dict[letter] += 1
    return frequency_dict