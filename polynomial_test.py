from Polynomial import *


def test_constructor():
    e1 = Expression.Expression(1, 2, 0, lambda x: x**2)
    e2 = Expression.Expression(1, 3, 0, lambda x: x**3)
    e3 = Expression.Expression(2, 2, 0, lambda x: 2*x**2)
    p = Polynomial([e1, e2, e3])
    print(p)


test_constructor()
