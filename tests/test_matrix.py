from danielutils import TestFactory, Test
from python_la.la1.Matrix import *
from python_la import VectorSpace, RealField
COUNT = 100
N = 50
V = VectorSpace(RealField(N))

m1 = Matrix([
    [2, 0, -2, -2],
    [0, 0, 1, 1],
    [0, -2, 3, 1],
    [0, 2, -3, -1]
])
m2 = Matrix([
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [-1, -1, 0, 0],
    [0, 1, 2, 1]
])


def test___init__():
    assert TestFactory(Matrix.__init__).add_tests([

    ])()


def test___getitem__():
    assert TestFactory(Matrix.__getitem__).add_tests([

    ])()


def test___setitem__():
    assert TestFactory(Matrix.__setitem__).add_tests([

    ])()


def test___str__():
    assert TestFactory(Matrix.__str__).add_tests([

    ])()


def test___add__():
    assert TestFactory(Matrix.__add__).add_tests([

    ])()


def test___neg__():
    assert TestFactory(Matrix.__neg__).add_tests([

    ])()


def test___sub__():
    assert TestFactory(Matrix.__sub__).add_tests([

    ])()


def test___mul__():
    assert TestFactory(Matrix.__mul__).add_tests([

    ])()


def test___rmul__():
    assert TestFactory(Matrix.__rmul__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(Matrix.__eq__).add_tests([

    ])()


def test___ne__():
    assert TestFactory(Matrix.__ne__).add_tests([

    ])()


def test___len__():
    assert TestFactory(Matrix.__len__).add_tests([

    ])()


def test___pow__():
    assert TestFactory(Matrix.__pow__).add_tests([

    ])()


def test___iter__():
    assert TestFactory(Matrix.__iter__).add_tests([

    ])()


def test_fromVector():
    assert TestFactory(Matrix.fromVector).add_tests([
    ])()


def test_from_vectors():
    assert TestFactory(Matrix.from_vectors).add_tests([

    ])()


def test_random():
    assert TestFactory(Matrix.random).add_tests([

    ])()


def test_from_jordan_blocks():
    assert TestFactory(Matrix.from_jordan_blocks).add_tests([

    ])()


def test_create_jordan_blcok():
    assert TestFactory(Matrix.create_jordan_blcok).add_tests([

    ])()


def test_identity():
    assert TestFactory(Matrix.identity).add_tests([
        Test(2, Matrix([[1, 0], [0, 1]], RealField(2))),
    ])()


def test_kernel():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).kernel
    assert TestFactory(inner).add_tests([

    ])()


def test_image():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).image
    assert TestFactory(inner).add_tests([

    ])()


def test_adjugate():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).adjugate
    assert TestFactory(inner).add_tests([

    ])()


def test_row_space():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).row_space
    assert TestFactory(inner).add_tests([

    ])()


def test_column_space():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).column_space
    assert TestFactory(inner).add_tests([

    ])()


def test_rank():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).rank
    assert TestFactory(inner).add_tests([
        Test(([[1, 0], [0, 1]], RealField(2)), 2),
        Test(([[1, 1], [0, 1]], RealField(2)), 2),
        Test(([[1, 1], [1, 1]], RealField(2)), 1),
        Test(([[1, 0], [1, 0]], RealField(2)), 1),
        Test(([[1, 1], [0, 0]], RealField(2)), 1),
    ])()


def test_determinant():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).determinant
    assert TestFactory(inner).add_tests([
        Test(([[1, 1], [1, 1]], RealField(2)), 0),
        Test(([[1, 0], [0, 1]], RealField(2)), 1),
        Test(([[1, 0], [1, 0]], RealField(2)), 0),
    ])()


def test_is_invertiable():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_invertiable
    assert TestFactory(inner).add_tests([

    ])()


def test_inverse():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).inverse
    assert TestFactory(inner).add_tests([

    ])()


def test_is_square():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_square
    assert TestFactory(inner).add_tests([

    ])()


def test_is_symmetrical():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_symmetrical
    assert TestFactory(inner).add_tests([

    ])()


def test_is_asymmetrical():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_asymmetrical
    assert TestFactory(inner).add_tests([

    ])()


def test_conjugate_transpose():
    def inner(*args, **kwargs): return Matrix(*
                                              args, **kwargs).conjugate_transpose
    assert TestFactory(inner).add_tests([

    ])()


def test_is_diagonialable():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_diagonialable
    assert TestFactory(inner).add_tests([

    ])()


def test_is_projection():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_projection
    assert TestFactory(inner).add_tests([

    ])()


def test_is_nilpotent():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).is_nilpotent
    assert TestFactory(inner).add_tests([

    ])()


def test_eigenvalues():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).eigenvalues
    assert TestFactory(inner).add_tests([

    ])()


def test_jordan_form():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).jordan_form
    assert TestFactory(inner).add_tests([

    ])()


def test_chain_basis():
    def inner(*args, **kwargs): return Matrix(*args, **kwargs).chain_basis
    assert TestFactory(inner).add_tests([

    ])()


def test_characteristic_polynomial():
    def inner(*args, **kwargs): return Matrix(*args,
                                              **kwargs).characteristic_polynomial
    assert TestFactory(inner).add_tests([

    ])()


def test_minimal_polynomial():
    def inner(*args, **kwargs): return Matrix(*
                                              args, **kwargs).minimal_polynomial
    assert TestFactory(inner).add_tests([

    ])()


def test_cofactor():
    assert TestFactory(Matrix.cofactor).add_tests([

    ])()


def test_minor():
    assert TestFactory(Matrix.minor).add_tests([

    ])()


def test_transpose():
    assert TestFactory(Matrix.transpose).add_tests([

    ])()


def test_conjugate():
    assert TestFactory(Matrix.conjugate).add_tests([

    ])()


def test_reorgenize_rows():
    assert TestFactory(Matrix.reorgenize_rows).add_tests([

    ])()


def test_apply_operation():
    assert TestFactory(Matrix.apply_operation).add_tests([

    ])()


def test_concat():
    assert TestFactory(Matrix.concat).add_tests([

    ])()


def test_split():
    assert TestFactory(Matrix.split).add_tests([

    ])()


def test_duplicate():
    assert TestFactory(Matrix.duplicate).add_tests([

    ])()


def test_gaussian_elimination_with():
    assert TestFactory(Matrix.gaussian_elimination_with).add_tests([

    ])()


def test_gaussian_elimination():
    assert TestFactory(Matrix.gaussian_elimination).add_tests([
        Test(m1, Matrix.identity(4)),
    ])()


def test_vectorize():
    assert TestFactory(Matrix.vectorize).add_tests([

    ])()


def test_solve():
    assert TestFactory(Matrix.solve).add_tests([

    ])()


def test_get_eigen_vectors_of():
    assert TestFactory(Matrix.get_eigen_vectors_of).add_tests([

    ])()


def test_algebraic_multiplicity():
    assert TestFactory(Matrix.algebraic_multiplicity).add_tests([

    ])()


def test_geometric_multiplicity():
    assert TestFactory(Matrix.geometric_multiplicity).add_tests([

    ])()
