from ...la1 import Matrix, RealField, VectorSpace, Vector

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


def test_from_vector():
    for _ in range(COUNT):
        v = V.random()
        m = Matrix.fromVector(v)
        for i in range(len(v)):
            assert v[i] == m[i][0]


def test_rank():
    assert Matrix.identity(10).rank == 10
    assert Matrix([[1, 1], [0, 0]]).rank == 1 == Matrix([[1, 0], [1, 0]]).rank


def test_from_vectors():
    for _ in range(int(COUNT/10)+1):
        vecs = [V.random() for _ in range(10)]
        m = Matrix.from_vectors(vecs)
        for i in range(len(vecs[0])):
            for j in range(len(vecs)):
                assert vecs[j][i] == m[i][j]


def test_determinant():
    assert Matrix([[1, 1], [1, 1]]).determinant == 0


def test_id():
    assert Matrix.identity(2) == Matrix([[1, 0], [0, 1]])


def test_guassian_elimination():
    assert Matrix([[1, 1], [1, 1]]).gaussian_elimination_with(
    )[0] == Matrix([[1, 1], [0, 0]])
    assert Matrix.identity(5).gaussian_elimination_with(
    )[0] == Matrix.identity(5)


def test_solve():
    assert Matrix([[1, 3], [2, 5]]).solve(
        Vector([1, 2])) == Vector([1, 0])
    assert Matrix([[1, 1], [1, 1]]).solve(Vector([1, 2])) == None
    assert Matrix.identity(2).solve(Vector([0, 0])) == Vector([0, 0])
    from ..Span import Span
    assert Matrix([[1, 1], [1, 1]]).solve(
        Vector([0, 0])) == Span([Vector([-1, 1])])


def test_kernel():
    from ..Span import Span
    from ..Vector import Vector
    assert Matrix([[1, 0], [0, 0]]).kernel == Span([Vector([0, 1])])
    assert Matrix([[1, 2, 3], [0, 1, 4]]).kernel == Span([Vector([5, -4, 1])])
    assert Matrix([[1, 2], [0, 0]]).kernel == Span([Vector([-2, 1])])
    assert Matrix([[2, 1], [0, 0]]).kernel == Span([Vector([-0.5, 1])])
    assert Span.are_same_span(Matrix([[1, 2, 3], [0, 0, 0]]).kernel, Span(
        [Vector([-3, 0, 1]), Vector([-2, 1, 0])]))


def test_eigenvalues():
    assert m1.eigenvalues.count(0) == 2
    assert m1.eigenvalues.count(2) == 2
    assert len(m1.eigenvalues) == 4


def test_algebraic_multiplicity():
    assert m1.algebraic_multiplicity(0) == 2
    assert m1.algebraic_multiplicity(2) == 2


def test_geometric_multiplicity():
    assert m1.geometric_multiplicity(0) == 1
    assert m1.geometric_multiplicity(2) == 2
