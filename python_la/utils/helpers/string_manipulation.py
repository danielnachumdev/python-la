from typing import Tuple, Any

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


def split_not_between_brackets(input: str, symbols: list[str]) -> list[str]:
    input = insert_multiplication(input)
    indecies = []
    stack = []
    split_indecies = []
    open_i = 0
    for i, c in enumerate(input):
        if c in symbols:
            split_indecies.append(i)
        if c in open_brackets:
            stack.append(c)
            open_i = i
        elif c in close_brackets:
            if stack[-1] == bracket_pairs[c]:
                stack.pop()
            if len(stack) == 0:
                indecies.append((open_i, i))
    # remove indecies that are inside brackets
    i = 0
    while i < len(split_indecies):
        index = split_indecies[i]
        for j in indecies:
            if j[0] < index < j[1]:
                split_indecies.remove(index)
                i -= 1
                break
        i += 1
    # split
    res = []
    order = []
    start = 0
    for end in range(len(input)):
        if end in split_indecies:
            order.append(input[end])
            res.append(input[start:end].strip())
            start = end+1
    res.append(input[start:].strip())
    return res, order


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


def split_many(lst: list[str], mark: str) -> list[str]:
    res = []
    for s in lst:
        res.extend(s.split(mark))
    return res


def split_if_any(string: str, marks: list[str]) -> Tuple[list[str], list[str]]:
    splits = []
    order = []
    start = 0
    for end, c in enumerate(string):
        if c in marks:
            splits.append(string[start:end].strip())
            order.append(c)
            start = end+1
    splits.append(string[start:].strip())
    return splits, order
