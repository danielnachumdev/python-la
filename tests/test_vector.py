from danielutils import TestFactory, Test
from python_la.la1.Vector import *


def test___init__():
    assert TestFactory(Vector.__init__).add_tests([

    ])()


def test___str__():
    assert TestFactory(Vector.__str__).add_tests([

    ])()


def test___add__():
    assert TestFactory(Vector.__add__).add_tests([

    ])()


def test___radd__():
    assert TestFactory(Vector.__radd__).add_tests([

    ])()


def test___sub__():
    assert TestFactory(Vector.__sub__).add_tests([

    ])()


def test___rsub__():
    assert TestFactory(Vector.__rsub__).add_tests([

    ])()


def test___neg__():
    assert TestFactory(Vector.__neg__).add_tests([

    ])()


def test___mul__():
    assert TestFactory(Vector.__mul__).add_tests([

    ])()


def test___rmul__():
    assert TestFactory(Vector.__rmul__).add_tests([

    ])()


def test___truediv__():
    assert TestFactory(Vector.__truediv__).add_tests([

    ])()


def test___rtruediv__():
    assert TestFactory(Vector.__rtruediv__).add_tests([

    ])()


def test___getitem__():
    assert TestFactory(Vector.__getitem__).add_tests([

    ])()


def test___setitem__():
    assert TestFactory(Vector.__setitem__).add_tests([

    ])()


def test___iter__():
    assert TestFactory(Vector.__iter__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(Vector.__eq__).add_tests([

    ])()


def test___ne__():
    assert TestFactory(Vector.__ne__).add_tests([

    ])()


def test___len__():
    assert TestFactory(Vector.__len__).add_tests([

    ])()


def test___hash__():
    assert TestFactory(Vector.__hash__).add_tests([

    ])()


def test_random():
    assert TestFactory(Vector.random).add_tests([

    ])()


def test_from_size():
    assert TestFactory(Vector.from_size).add_tests([

    ])()


def test_e():
    assert TestFactory(Vector.e).add_tests([

    ])()


def test_conjugate():
    def inner(): Vector().conjugate
    assert TestFactory(inner).add_tests([

    ])()


def test_norm():
    assert TestFactory(Vector.norm).add_tests([

    ])()


def test_dot():
    assert TestFactory(Vector.dot).add_tests([

    ])()


def test_normalize():
    assert TestFactory(Vector.normalize).add_tests([

    ])()


def test_projection_onto():
    assert TestFactory(Vector.projection_onto).add_tests([

    ])()


def test_duplicate():
    assert TestFactory(Vector.duplicate).add_tests([

    ])()
