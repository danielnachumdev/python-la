from .string_manipulation import bracket_pairs


def string_splitter(lst: list[str], symbol: str, excluders: list[str] = list(bracket_pairs.keys())) -> list[str]:
    res = []
    for string in lst:
        res.extend(string.strip().split(symbol))
    return res


def stacker(string: str, lst: list[str]) -> list[str]:
    res = []
    for c in string:
        if c in lst:
            res.append(c)
    return res


def sign(op):
    if op is '+':
        return 1
    return -1
