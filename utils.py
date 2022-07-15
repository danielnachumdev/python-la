import math


def are_operators_implemnted(T) -> bool:
    try:
        T.__add__
        T.__radd__
        T.__sub__
        T.__neg__
        T.__mul__
        T.__rmul__
        T.__truediv__
        T.__rtruediv__
        T.__eq__
        T.__ne__
        return True
    except AttributeError:
        return False


def almost_equal(*args):
    # THRESHOLD = 0.000000000001
    # def compare_two(a, b) -> bool:
    #     # if b == 0:
    #     #     try:
    #     #         return a < THRESHOLD
    #     #     except:
    #     #         return a == 0
    #     # if a == 0:
    #     #     try:
    #     #         return b < THRESHOLD
    #     #     except:
    #     #         return b == 0
    #     if abs(a) > 100000 and abs(b) > 100000:
    #         return abs(1-a/b) < THRESHOLD
    #     return abs(a-b) < THRESHOLD
    # return all([compare_two(args[0], args[i]) for i in range(1, len(args))])

    return all([math.isclose(args[0], args[i]) for i in range(1, len(args))])


def areinstances(arr: list, T):
    return check_foreach(arr, lambda v: isinstance(v, T))


def isoneof(v, lst: list) -> bool:
    for T in lst:
        if isinstance(v, T):
            return True
    return False


def alloneof(value: list, types: list):
    for v in value:
        if not isoneof(v, types):
            return False
    return True


def check_foreach(arr: list, condition) -> bool:
    for v in arr:
        if not condition(v):
            return False
    return True


def validate_brackets(s: str) -> bool:
    if len(s) == 0:
        return True
    brackets = ["(", ")", "[", "]", "{", "}"]
    stack = []
    for c in s:
        if c in brackets:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != brackets[brackets.index(c)-1]:
                    return False
                stack.pop()
    return len(stack) == 0
