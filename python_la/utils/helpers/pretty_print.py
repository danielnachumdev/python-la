
from ..helpers import split_many, areinstances, split_if_any
from .math_symbols import python_la_superscript_n, subscript_n


def python_la_is_number(string: str) -> bool:
    for s in string:
        if s not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True


def __get_superscript(string: str) -> str:
    res = ""
    j = string.index("^")
    num = string[j+1:]
    if python_la_is_number(num):
        res += string[:j]
        res += python_la_superscript_n(int(num))
    else:
        res += string
    return res


def __get_subscript(string: str) -> str:
    res = ""
    j = string.index("_")
    i = len(string)
    if "^" in string:
        i = string.index("^")
    num = string[j+1:i]
    if python_la_is_number(num):
        res += string[:j]
        res += subscript_n(int(num))
    else:
        res += string
    return res


def reorder_multiplication(string: str) -> str:

    mul = "*"
    div = "/"
    if not any([op in string for op in [mul, div]]):
        return string
    res = ""
    splits, operators = split_if_any(string, [mul, div])
    for i, op in enumerate(operators):
        if op == mul:
            res += splits[i+1]+op+splits[i]
        else:
            res += "1/"+splits[i+1]+"*"+splits[i]
    return res


def reorder_str(string: str) -> str:
    res = ""
    addition = ["+", "-"]
    splits, order = split_if_any(string, addition)
    splits = [reorder_multiplication(s) for s in splits]
    if len(order) == 0:
        return splits[0]
    for i, op in enumerate(order):
        res += splits[i]+" "+op+" "
    res += splits[-1]
    return res


def pretty_str(string: str) -> str:
    string = reorder_str(string)
    res = ""
    splits, addition_order = split_if_any(string, ["+", "-"])
    for index, s in enumerate(splits):
        i = 0
        breakers = ["^", "_"]
        while i < len(s):
            c = s[i]
            if c in breakers:
                j = 1
                while i+j < len(s) and s[i+j] not in breakers:
                    j += 1
                if c == "^":
                    res += python_la_superscript_n(s[i+1:i+j])
                elif c == "_":
                    res += subscript_n(s[i+1:i+j])
                i += j - 1
            else:
                res += c
            i += 1
        if index != len(splits)-1:
            res += " " + addition_order[index] + " "
    return res


def pretty_print(*args: list[str], **kwargs) -> None:
    if not areinstances([*args], str):
        raise TypeError("s must be a string")
    result = []
    for string in args:
        result.append(pretty_str(string))
    print(*result, **kwargs)
