

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


def areinstances(arr: list, T):
    for o in arr:
        if not isinstance(o, T):
            return False
    return True
