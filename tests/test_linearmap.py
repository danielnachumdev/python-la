from danielutils import TestFactory, Test
from python_la.la1.LinearMap import *
from python_la.la1 import RealField, Vector
R3 = RealField(4)
R2 = RealField(2)
T = LinearMap.from_fields(R2, R2, lambda v: Vector([v[1], v[0]], R2))


def test___init__():
    assert TestFactory(LinearMap.__init__).add_tests([

    ])()


def test___add__():
    assert TestFactory(LinearMap.__add__).add_tests([
        Test((T, T), T*2)
    ])()


def test___radd__():
    assert TestFactory(LinearMap.__radd__).add_tests([

    ])()


def test___sub__():
    from python_la import Matrix
    A = LinearMap.from_matrix(Matrix([[1, -1], [-1, 1]]))
    TestFactory(LinearMap.__sub__).add_tests([
        Test((LinearMap.from_fields(
            R2, R2, lambda v: Vector([v[0], v[1]], R2)), T), A)
    ])()


def test___rsub__():
    assert TestFactory(LinearMap.__rsub__).add_tests([

    ])()


def test___neg__():
    assert TestFactory(LinearMap.__neg__).add_tests([

    ])()


def test___mul__():
    T2 = LinearMap.from_fields(R2, R2, lambda v: v)
    assert TestFactory(LinearMap.__mul__).add_tests([
        Test((T, 1), T),
        Test((T, 0), T-T),
        Test((T2, T), T*T2),
    ])()


def test___rmul__():
    assert TestFactory(LinearMap.__rmul__).add_tests([

    ])()


def test___pow__():
    assert TestFactory(LinearMap.__pow__).add_tests([
        Test((T, 11), T),
        Test((T, 1), T),
    ])()


def test___eq__():
    assert TestFactory(LinearMap.__eq__).add_tests([

    ])()


def test___call__():
    assert TestFactory(LinearMap.__call__).add_tests([

    ])()


def test_is_func_linear_map():
    assert TestFactory(LinearMap.is_func_linear_map).add_tests([

    ])()


def test_from_matrix():
    assert TestFactory(LinearMap.from_matrix).add_tests([

    ])()


def test_from_fields():
    assert TestFactory(LinearMap.from_fields).add_tests([

    ])()


def test_id():
    assert TestFactory(LinearMap.id).add_tests([

    ])()


def test_to_matrix():
    assert TestFactory(LinearMap.to_matrix).add_tests([

    ])()
