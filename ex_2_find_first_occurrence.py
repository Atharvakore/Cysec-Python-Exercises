def find_first_occurrence(haystack: str, needle: str) -> int | bool:
    offset = haystack.find(needle)
    if offset == -1:
        return False
    return offset