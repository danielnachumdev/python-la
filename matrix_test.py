from Matrix import Matrix
from Field import RealField, Fields

COUNT = 100
N = 50
Fn = RealField(Fields.R, 0, 1, N, 1)


def test_from_vector():
    for _ in range(COUNT):
        v = Fn.random()
        m = Matrix.fromVector(v)
        for i in range(v.length):
            assert v[i] == m[i][0]


def test_from_vectors():
    for _ in range(int(COUNT/10)+1):
        vecs = [Fn.random() for _ in range(10)]
        m = Matrix.fromVectors(vecs)
        for i in range(len(vecs[0])):
            for j in range(len(vecs)):
                assert vecs[j][i] == m[i][j]
