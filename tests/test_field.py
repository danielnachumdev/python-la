from danielutils import TestFactory, Test
from python_la.la1.Field import *


def test_is_field():
    assert TestFactory(Field.is_field).add_tests([
        Test(ComplexField(), True),
        Test(RationalField(), True),
        Test(RealField(), True),
    ])()


def test___init__():
    assert TestFactory(Field.__init__).add_tests([

    ])()


def test___str__():
    assert TestFactory(Field.__str__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(Field.__eq__).add_tests([

    ])()


def test_random():
    assert TestFactory(Field.random).add_tests([

    ])()


def test___contains__():
    assert TestFactory(Field.__contains__).add_tests([

    ])()
