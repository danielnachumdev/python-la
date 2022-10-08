from danielutils import TestFactory, Test
from python_la.la1.VectorSpace.VectorSpace import *


def test___init__():
    assert TestFactory(VectorSpace.__init__).add_tests([

    ])()


def test___str__():
    assert TestFactory(VectorSpace.__str__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(VectorSpace.__eq__).add_tests([

    ])()


def test___ne__():
    assert TestFactory(VectorSpace.__ne__).add_tests([

    ])()


def test___contains__():
    assert TestFactory(VectorSpace.__contains__).add_tests([

    ])()


def test_random():
    assert TestFactory(VectorSpace.random).add_tests([

    ])()


def test_e():
    assert TestFactory(VectorSpace.e).add_tests([

    ])()


def test_standard_basis():
    assert TestFactory(VectorSpace.standard_basis).add_tests([

    ])()
