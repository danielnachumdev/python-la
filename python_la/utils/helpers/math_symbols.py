# https://unicode-table.com/en/sets/mathematical-signs/
python_la_double_n = "ℕ"
python_la_double_q = "ℚ"
python_la_double_r = "ℝ"
python_la_double_z = "ℤ"
python_la_double_c = "ℂ"
python_la_rpab = "〉"  # right pointing angle bracket
python_la_lpab = "〈"  # left pointing angle bracket
python_la_forall = "∀"
python_la_exists = "∃"
python_la_vl = "|"
python_la_sigma = "∑"
python_la_pi = "∏"
python_la_circled_plus = "⊕"
python_la_ne = "≠"
python_la_equiv = "≡"
python_la_lamda = "λ"
python_la_superscript_left_parenthesis = "⁽"
python_la_superscript_right_parenthesis = "⁾"
python_la_superscript_plus = "⁺"
python_la_superscript_minus = "⁻"
python_la_superscript_equals = "⁼"
python_la_superscript_0 = "⁰"
python_la_superscript_1 = "¹"
python_la_superscript_2 = "²"
python_la_superscript_3 = "³"
python_la_superscript_4 = "⁴"
python_la_superscript_5 = "⁵"
python_la_superscript_6 = "⁶"
python_la_superscript_7 = "⁷"
python_la_superscript_8 = "⁸"
python_la_superscript_9 = "⁹"
python_la_superscript_digits = [python_la_superscript_0, python_la_superscript_1, python_la_superscript_2, python_la_superscript_3,
                                python_la_superscript_4, python_la_superscript_5, python_la_superscript_6, python_la_superscript_7, python_la_superscript_8, python_la_superscript_9]


def python_la_superscript_n(n) -> str: return "".join(
    [python_la_superscript_digits[int(i)] for i in str(n)])


subscript_0 = "\u2080"
subscript_1 = "\u2081"
subscript_2 = "\u2082"
subscript_3 = "\u2083"
subscript_4 = "\u2084"
subscript_5 = "\u2085"
subscript_6 = "\u2086"
subscript_7 = "\u2087"
subscript_8 = "\u2088"
subscript_9 = "\u2089"
subscript_plus = "\u208A"
subscript_minus = "\u208B"
subscript_equals = "\u208C"
subscript_left_parenthesis = "\u208D"
subscript_right_parenthesis = "\u208E"
subscript_digits = [subscript_0, subscript_1, subscript_2, subscript_3,
                    subscript_4, subscript_5, subscript_6, subscript_7, subscript_8, subscript_9]


def subscript_n(n: int) -> str:
    return "".join(
        [subscript_digits[int(i)] for i in str(n)])


python_la_square_root = "√"
python_la_cube_root = "∛"
python_la_forth_root = "∜"


def python_la_nth_root(n: int) -> str:
    if n == 1 or n == 0:
        raise ValueError("n must not be 0,1")
    if n == 2:
        return python_la_square_root
    if n == 3:
        return python_la_cube_root
    if n == 4:
        return python_la_forth_root
    return python_la_superscript_n(n)+python_la_square_root
