from __future__ import annotations
from utils import almost_equal
from typing import Any, Union
from Complex import Complex
import Vector
import Span
import Field
import copy
import functools
import SimplePolynomial
from utils import areinstances, check_foreach, isoneof
t_matrix = list[list[Union[float, Complex]]]


class Matrix:

    @staticmethod
    def fromVector(vec: Vector.Vector, sol: Vector.Vector = None) -> Matrix:
        """
        will add the vector as a column
        """
        # return Matrix.fromVectors([vec])
        return Matrix([[v] for v in vec], sol)

    @staticmethod
    def fromSpan(span: Span.Span, sol: Vector.Vector) -> Matrix:
        """
        will create a matrix from the span in the order that the vectors appear and as columns
        """
        if not isinstance(span, Span.Span):
            raise TypeError("span must be 'Span'")
        return Matrix.fromVectors([v for v in span], sol)

    @staticmethod
    def fromVectors(vecs: list[Vector.Vector], sol: Vector.Vector = None) -> Matrix:
        """
        will create a amtrix from the vectors in the order they appear and as columns
        """
        if not areinstances(vecs, Vector.Vector):
            raise TypeError("all elements must be instances of class 'Vector'")
        if not check_foreach(vecs, lambda v: v.field == vecs[0].field):
            raise ValueError("vectors are not over the same field")
        mat = []
        for i in range(vecs[0].length):
            mat.append([])
            for j in range(len(vecs)):
                mat[i].append(vecs[j][i])
        return Matrix(mat, sol, field=vecs[0].field)

    @staticmethod
    def fromString(matrix_string: str, sol: Vector.Vector) -> Matrix:
        return Matrix([[int(num) for num in row.split()]
                       for row in matrix_string.split("\n")], sol)

    @staticmethod
    def random(f: Field.Field = None, min: float = -10, max: float = 10, degree: int = 10,  def_value=None) -> Matrix:
        if f is None:
            f = Field.DefaultRealField
        # TODO how to check that defualt value is inside 'f'? what if 'f' is ratinals and has no __contains__ implemented?
        return Matrix([[f.random(min, max) if def_value is None else def_value for _ in range(degree)]for __ in range(degree)], field=f)

    @staticmethod
    def fromJordanBlocks(lst: list[Matrix]) -> Matrix:
        pass

    @staticmethod
    def createJordanBlock(size: int, eigenvalue) -> Matrix:
        pass

    @staticmethod
    def id_matrix(size: int) -> Matrix:
        arr = [[0 for __ in range(size)] for _ in range(size)]
        for i in range(size):
            arr[i][i] = 1
        return Matrix(arr)

    def __init__(self, mat: t_matrix, sol_vec: list[Union[float, Complex]] = None, field: Field.Field = None) -> None:
        if field is None:
            field = Field.DefaultRealField
        self.__matrix = mat
        self.__rows = len(mat)
        self.__cols = len(mat[0])
        self.__solution_vector = sol_vec if sol_vec else [
            0 for _ in range(self.__rows)]
        self.field = field

    @property
    def kernel(self) -> Span.Span:
        solution = Matrix(
            self.__matrix, [0 for _ in range(self.__rows)]).solve()

    @property
    def image(self) -> Span.Span:
        # TODO implement image calculation
        pass

    @property
    def rank(self) -> int:
        self.reorgenize_rows()
        rank = 0
        for row in self.__matrix:
            if all([i == 0 for i in row]):
                continue
            rank += 1
        return rank

    @property
    def determinant(self) -> float:
        if self.__rows != self.__cols:
            raise ValueError("Matrix must be square")
        if self.__rows == 1:
            return self.__matrix[0][0]
        if self.__rows == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]
        return sum([self.__matrix[i][0] * ((-1)**i) * self.minor(i, 0) for i in range(self.__rows)])

    @property
    def is_invertiable(self) -> bool:
        return self.determinant != 0

    @property
    def is_square(self) -> bool:
        return self.__rows == self.__cols

    @property
    def is_diagonialable(self) -> bool:
        # TODO implement diagonialability check
        pass

    @property
    def is_nilpotent(self) -> bool:
        # TODO implement nilpotency check
        pass

    @property
    def eigen_values(self) -> Vector.Vector:
        # TODO implement eigen value calculation
        pass

    @property
    def jordan_form(self) -> Matrix:
        # TODO implement jordan form calculation
        pass

    @property
    def chain_basis(self) -> Span.Span:
        # TODO implement chain basis calculation
        pass

    @property
    def characteristic_polynomial(self) -> SimplePolynomial.SimplePolynomial:
        # TODO implement characteristic polynomial calculation
        pass

    @property
    def minimal_polynomial(self) -> SimplePolynomial.SimplePolynomial:
        # TODO implement minimal polynomial calculation
        pass

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        return self.__matrix[index]

    def __str__(self) -> str:
        result = ""
        for i, row in enumerate(self.__matrix):
            result += str(row)
            result += " | "+str(self.__solution_vector[i]) + "\n"
        return result

    def __add__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            raise TypeError("Matrix can only be added to another Matrix")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.__matrix[i][j] + other.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __neg__(self) -> Matrix:
        return Matrix([[-self.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __sub__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            raise TypeError(
                "Matrix can only be subtracted from another Matrix")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.__matrix[i][j] - other.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __mul__(self, other: Union[float, Complex, Vector.Vector, Matrix]) -> Union[float, Complex, Vector.Vector, Matrix]:
        """
        self * other
        """
        if isoneof(other, [int, float, Complex]):
            res = self
            for i in range(len(self)):
                for j in range(len(self[0])):
                    res[i][j] *= other
            return res
            # return Matrix([[other * self.__matrix[i][j] for j in range(len[self[0]])]
            #                for i in range(len(self))])
        if isinstance(other, Vector.Vector):
            if self.__cols != other.length:
                raise ValueError(
                    "Matrix and Vector must have the same number of rows")
            return Vector.Vector([sum([self.__matrix[i][j] * other[j] for j in range(self.__cols)])
                                  for i in range(self.__rows)])
        if isinstance(other, Matrix):
            if self.__cols != other.__rows:
                raise ValueError(
                    "Matrix and Matrix must have matching sizes: self.cols == other.rows")
            return Matrix([[sum([self.__matrix[i][j] * other.__matrix[j][k] for j in range(self.__cols)])
                            for k in range(other.__cols)] for i in range(self.__rows)])
        raise TypeError(
            "Matrix can only be multiplied by a number, Vector, or Matrix")

    def __rmul__(self, other: Union[int, float, Complex, Vector.Vector, Matrix]) -> Union[float, Complex, Vector.Vector, Matrix]:
        """
        other * self
        """
        if isoneof(other, [int, float, Complex]):
            return self.__mul__(other)
        if isinstance(other, Vector):
            raise TypeError(
                "Matrix can only be multiplied by a vector from the right")
        if isinstance(other, Matrix):
            if self.__cols != other.__rows:
                raise ValueError(
                    "Matrix and Matrix must have the same number of columns")
            return Matrix([[sum([self.__matrix[i][j] * other.__matrix[j][k] for j in range(self.__cols)])
                            for k in range(other.__cols)] for i in range(self.__rows)])
        raise TypeError(
            f"cant perform {type(other)}*Matrix.\ncan only be multiplied by a:\n\tint\n\tfloat\n\tComplex\n\tVector\n\tMatrix]")

    def __eq__(self, other: Matrix) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError(f"cant complare 'Matrix' with '{type(other)}'")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return False
        if any([self.__matrix[i][j] != other.__matrix[i][j] for i in range(self.__rows) for j in range(self.__cols)]):
            return False
        return True

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __len__(self) -> int:
        return self.__rows

    def __pow__(self, other) -> Matrix:
        if isoneof(other, [int, float]):
            if other == int(other):
                other = int(other)
                res = self
                for _ in range(other-1):
                    res *= self
                return res
            raise NotImplementedError(
                "Matrix**float is not implemented")
        raise NotImplementedError(
            f"Matrix power not implemented for Matrix**{type(other)}")

    def almost_equal(self, other: Matrix) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError("Matrix can only be compared to another Matrix")
        if not self.field == other.field:
            raise ValueError("Matrix must have the same field")
        return all([all([almost_equal(self[i][j], other[i][j])] for j in range(len(self[0]))) for i in range(len(self))])

    def inverse(self) -> Matrix:
        if not self.is_invertiable:
            raise ValueError("Matrix must be invertible")
        return Matrix([[self.minor(i, j) / self.determinant for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def cofactor(self, row_to_ignore: int, col_to_ignore: int) -> Matrix:
        if(row_to_ignore >= self.__rows or col_to_ignore >= self.__cols):
            raise ValueError("Row or column index out of range")
        res: t_matrix = []
        for i, row in enumerate(self.__matrix):
            if i == row_to_ignore:
                continue
            res.append([])
            for j, col in enumerate(self.__matrix[i]):
                if j == col_to_ignore:
                    continue
                res[i if i < row_to_ignore else i -
                    1].append(self.__matrix[i][j])
        return Matrix(res)

    def minor(self, row_to_ignore: int, col_to_ignore: int) -> float:
        return self.cofactor(row_to_ignore, col_to_ignore).determinant

    def transpose(self) -> Matrix:
        return Matrix([[self.__matrix[j][i] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def reorgenize_rows(self):
        def comparer(a: list[float], b: list[float]) -> bool:
            def first_not_zero_index(row: list[float]) -> int:
                for i in range(len(row)):
                    if row[i] != 0:
                        break
                return i
            return -1 if first_not_zero_index(a) > first_not_zero_index(b) else 1
        self.__matrix = sorted(
            self.__matrix, key=functools.cmp_to_key(comparer), reverse=True)

    def guassian_elimination(self, sol=None) -> Matrix:
        if not sol:
            sol = self.__solution_vector

        def first_not_zero_index(row: list[float]) -> int:
            for i in range(len(row)):
                if row[i] != 0:
                    break
            return i
        res = copy.deepcopy(self)
        res.__solution_vector = sol
        res.reorgenize_rows()
        # gaussian elimination
        for r in range(res.__rows):
            lead_index = first_not_zero_index(res[r])
            lead_value = res[r][lead_index]
            if lead_value == 0:
                continue
            if lead_value != 1:
                for c in range(res.__cols):
                    res[r][c] /= lead_value
                res.__solution_vector[r] /= lead_value
                lead_value = res[r][lead_index]
            for r2 in range(res.__rows):
                if r == r2:
                    continue
                row_divider = res[r2][lead_index]/lead_value
                if row_divider == 0:
                    continue
                for c in range(res.__cols):
                    res[r2][c] -= row_divider * res[r][c]
                res.__solution_vector[r2] -= row_divider * \
                    res.__solution_vector[r]
        return res

    def solve(self, vec=None) -> Union[Vector.Vector, Span.Span, None]:
        """
        Solve the system of equations
        """
        if self.__rows != self.__cols:
            raise ValueError("Matrix must be square")
        if vec == None:
            vec = self.__solution_vector
        if not isoneof(vec, [Vector.Vector, list]):
            raise TypeError("Matrix must be solved for a vector")
        result_matrix = self.guassian_elimination(list(vec))
        for i, row in enumerate(result_matrix):
            if (not Vector.Vector(row).has_no_zero) and result_matrix.__solution_vector[i] != 0:
                return None
        if result_matrix.rank != result_matrix.__rows:
            # FIXME
            # TODO implement solutions for nullity rank > 1
            raise NotImplementedError(
                "nullity rank was atleast 1, not yet implemented")
        else:
            return Vector.Vector(result_matrix.__solution_vector)

    def get_eigen_space_of(eigenvalue) -> Span:
        # TODO calculate the eigen space of an eigen value
        pass

    def algebraic_multiplicity(eigenvalue) -> int:
        # TODO calculate the algebraic multiplicity of an eigenvalue
        pass

    def geometric_multiplicity(eigenvalue) -> int:
        # TODO calculate the geometric multiplicity of an eigenvalue
        pass
