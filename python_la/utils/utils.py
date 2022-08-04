# import Complex

import math
from typing import Tuple, Any


def are_operators_implemnted(T) -> bool:
    try:
        T.__add__
        T.__radd__
        T.__sub__
        T.__rsub__
        T.__neg__
        T.__mul__
        T.__rmul__
        T.__truediv__
        T.__rtruediv__
        T.__eq__
        T.__ne__
        T.__hash__
        return True
    except AttributeError:
        return False


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


def almost_equal(*args):
    THRESHOLD = 0.000000000001
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

    def wrapper(a, b):
        if alloneof([a, b], [int, float]):
            return math.isclose(a, b, abs_tol=THRESHOLD)
        else:  # they are Complex.Complex
            try:
                return math.isclose(a.real, b.real, abs_tol=THRESHOLD) and math.isclose(a.imag, b.imag, abs_tol=THRESHOLD)
            except Exception as e:
                assert False, "shouldnt be here"
    return all([wrapper(args[0], args[i]) for i in range(1, len(args))])


def areinstances(arr: list, T):
    return check_foreach(arr, lambda v: isinstance(v, T))


def check_foreach(arr: list, condition) -> bool:
    for v in arr:
        if not condition(v):
            return False
    return True


bracket_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    ")": "(",
    "]": "[",
    "}": "{"
}


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


open_brackets = ["(", "[", "{"]
close_brackets = [")", "]", "}"]


def bracketify(input) -> list[Tuple[str, int]]:
    res = []
    for i, c in enumerate(input):
        if c in open_brackets+close_brackets:
            res.append((c, i))
    return res


def insert_multiplication(input: str) -> str:
    brackets = bracketify(input)
    stack = []
    # recent = None
    change = 0
    for i in range(len(brackets)-1):
        if brackets[i][0] in open_brackets:
            stack.append(brackets[i])
        elif brackets[i][0] in close_brackets:
            if stack[-1][0] == bracket_pairs[brackets[i][0]]:
                # recent = stack.pop()
                if brackets[i+1][0] in open_brackets and brackets[i+1][1] == brackets[i][1] + 1:
                    input = f"{input[:brackets[i][1]+1+change]}*{input[brackets[i][1]+1+change:]}"
                    change += 1
    return input


def open_power(input: str) -> str:
    stack = []
    i = 0
    change = 0
    while i < len(input)-1:
        c = input[i]
        if c in open_brackets:
            stack.append((c, i))
        else:
            if c in close_brackets:
                if stack[-1][0] == bracket_pairs[c]:
                    recent = stack.pop()
                    if input[i+1] == "^":
                        try:
                            # extract power end index
                            j = i+2
                            while j < len(input):
                                c2 = input[j]
                                if not c2.isdigit():
                                    break
                                j += 1
                            # parse power
                            power = int(input[i+2:j])
                            # amount of digits in the power
                            size = len(str(power))
                            # the text to insert 'power' times
                            text_to_insert = input[recent[1]:i+1]

                            # insertion
                            change = 0
                            for _ in range(power-1):
                                input = f"{input[:i+1+change]}{text_to_insert}{input[i+change+2+size:]}"
                                change += len(text_to_insert)
                            i += change
                        except Exception as e:
                            pass

        i += 1
    return input


def split_not_between_brackets(input: str, symbol: str) -> list[str]:
    input = insert_multiplication(input)
    indecies = [0]
    stack = []
    for i, c in enumerate(input):
        if c in open_brackets:
            stack.append(c)
        elif c in close_brackets:
            if stack[-1] == bracket_pairs[c]:
                stack.pop()
            if len(stack) == 0:
                indecies.append(i)
    res = []
    for i in range(len(indecies)-1):
        res.append(input[indecies[i]+1+2*i:indecies[i+1]])
    return res


def composite_function(f, g):
    return lambda *args: f(g(*args), *args[1:])


def concat_horizontally(lst: list[Any], sep: str = " ", end: str = "") -> str:
    res = ""
    strs = [str(v)for v in lst]
    prev_char_indecies = [0 for _ in range(len(lst))]
    char_indecies = [0 for _ in range(len(lst))]
    while sum(char_indecies) < sum([len(s) for s in strs]):
        # find indecies for each entry
        to_advance = set([i for i in range(len(lst))])
        to_remove = set()
        while len(to_advance) > 0:
            for i in to_advance:
                if strs[i][char_indecies[i]] == '\n':
                    to_remove.add(i)
                    continue
                char_indecies[i] += 1
            for v in to_remove:
                to_advance.remove(v)
            to_remove.clear()
        # print acordingly
        for vec_index in range(len(strs)):
            res += strs[vec_index][prev_char_indecies[vec_index]:char_indecies[vec_index]]+sep
            prev_char_indecies[vec_index] = char_indecies[vec_index]+1
            char_indecies[vec_index] += 1
        res += "\n"
    return res+end
