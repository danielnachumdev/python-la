import random
from ...la1 import VectorSpace, Matrix, RealField
from ...la2 import BilinearForm, StandardInnerProduct as sip


def test_standard_gram_matrix():
    n = random.randint(1, 10)
    Vr2 = VectorSpace(RealField(n))
    g = BilinearForm(lambda x, y: sip(x, y), Vr2)
    assert g.toMatrix() == Matrix.id_matrix(n)
