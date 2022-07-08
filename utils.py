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
    THRESHOLD = 0.000000000001

    def compare_two(a, b) -> bool:
        if b == 0:
            try:
                return a < THRESHOLD
            except:
                return a == 0
        if a == 0:
            try:
                return b < THRESHOLD
            except:
                return b == 0
        return abs(1-a/b) < THRESHOLD

    return all([compare_two(args[0], args[i]) for i in range(1, len(args))])
