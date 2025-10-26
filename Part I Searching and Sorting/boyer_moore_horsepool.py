# Here is a clean reference implementation of the Horspool (Boyer-Moore–Horspool) substring search in Python.
# It returns the index of the first match or -1 if not found.

def build_bad_match_table(pattern: str):
    """
    Build Horspool bad match table.
    shift[c] = how far to shift when mismatch occurs at last char.
    Only pattern[0..m-2] are used.
    """
    m = len(pattern)
    table = { }           # dict mapping char → shift distance

    # fill from indices 0..m-2
    for i in range(m - 1):
        table[pattern[i]] = (m - 1) - i

    # any char not in table should shift full length
    # we will handle that by table.get(c, m) when using it
    return table


def horspool(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0  # empty pattern matches at 0

    table = build_bad_match_table(pattern)

    i = m - 1  # index in text aligned with last char of pattern
    while i < n:
        k = 0
        # try to match backward from last char
        while k < m and text[i - k] == pattern[m - 1 - k]:
            k += 1

        if k == m:
            return i - (m - 1)  # full match

        # mismatch at text[i - k], shift using that char
        c = text[i]
        shift = table.get(c, m)
        i += shift

    return -1




# Example usage

txt = "here is a simple example"
pat = "example"

idx = horspool(txt, pat)
print(idx)  # 17 if using this exact string


