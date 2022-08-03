from __future__ import annotations
from typing import Any, Union
import enum
import copy
import functools
from typing import Tuple
from ..utils import almost_equal
from .Complex import Complex
from .Vector import Vector
from .Field import Field, DefaultRealField
from ..utils import areinstances, check_foreach, isoneof

# TODO remove hardcoded solution vec and add it as parameter to solve with


class MatrixOperationType(enum.Enum):
    ROW_SWITCHING = "row_switching"
    ROW_MULTIPLICATION = "row_multiplication"
    ROW_ADDITION = "row_addition"
    COL_SWITCHING = "column_switching"
    COL_MULTIPLICATION = "column_multiplication"
    COL_ADDITION = "column_addition"


MOT = MatrixOperationType


# class MatrixOperation:
#     def __init__(self, operation_type: MatrixOperationType, iv1: Union[int, float], iv2: Union[int, float]):
#         self.operation_type = operation_type
#         self.iv1, self.iv2 = iv1, iv2

#     def __call__(self, matrix, operate_with: Union[Vector, Matrix] = None) -> Tuple[Matrix, Union[Vector, Matrix]]:
#         res = matrix
#         iv1, iv2 = self.iv1, self.iv2
#         match(self.operation_type):
#             case MatrixOperationType.ROW_SWITCHING:
#                 res[iv1], res[iv2] = res[iv2], res[iv1]
#             case MatrixOperationType.COL_SWITCHING:
#                 for i in range(len(res[0])):
#                     res[i][iv1], res[i][iv2] = res[i][iv2], res[i][iv1]
#             case MatrixOperationType.ROW_MULTIPLICATION:
#                 res[iv1] = [iv2*v for v in res[iv1]]
#             case MatrixOperationType.COL_MULTIPLICATION:
#                 for i in range(len(res[0])):
#                     res[i][iv1] *= iv2
#             case MatrixOperationType.ROW_ADDITION:
#                 res[iv1] = [res[iv1][i]+res[iv2][i]
#                             for i in range(len(res[iv1]))]
#             case MatrixOperationType.COL_ADDITION:
#                 for i in range(len(res[0])):
#                     res[i][iv1] += res[i][iv2]
#         return res, operate_with


class Matrix:

    @staticmethod
    def fromVector(vec: Vector, sol: Vector = None) -> Matrix:
        """
        will add the vector as a column
        """
        # return Matrix.fromVectors([vec])
        return Matrix([[v] for v in vec], sol)

    @staticmethod
    def fromVectors(vecs: list[Vector], sol: Vector = None) -> Matrix:
        """
        will create a amtrix from the vectors in the order they appear and as columns
        """
        if not areinstances(vecs, Vector):
            raise TypeError("all elements must be instances of class 'Vector'")
        if not check_foreach(vecs, lambda v: v.field == vecs[0].field):
            raise ValueError("vectors are not over the same field")
        mat: list[list[Any]] = []
        for i in range(vecs[0].length):
            mat.append([])
            for j in range(len(vecs)):
                mat[i].append(vecs[j][i])
        return Matrix(mat, sol, field=vecs[0].field)

    @staticmethod
    def fromString(matrix_string: str, sol: Vector) -> Matrix:
        return Matrix([[int(num) for num in row.split()]
                       for row in matrix_string.split("\n")], sol)

    @staticmethod
    def random(rows: int, cols: int, f: Field = None, min: float = -10, max: float = 10, degree: int = 10,  def_value=None) -> Matrix:
        if f is None:
            f = DefaultRealField
        # TODO how to check that defualt value is inside 'f'? what if 'f' is ratinals and has no __contains__ implemented?
        return Matrix([[f.random(min, max) if def_value is None else def_value for _ in range(cols)]for __ in range(rows)], field=f)

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

    def __init__(self, mat: list[list[Any]], sol_vec: list[Union[float, Complex]] = None, field: Field = DefaultRealField) -> None:
        if not isinstance(mat, list) or not all([isinstance(v, list) for v in mat]):
            raise TypeError("Matrix must be a 2d array")
        self.__matrix = mat
        self.__rows = len(mat)
        self.__cols = len(mat[0])
        self.__solution_vector = sol_vec if sol_vec else [
            0 for _ in range(self.__rows)]
        self.field = field

    @property
    def kernel(self) -> list[Vector]:
        solution = Matrix(
            self.__matrix, [0 for _ in range(self.__rows)]).solve()

    @property
    def image(self) -> list[Vector]:
        # TODO implement image calculation
        pass

    @property
    def rank(self) -> int:
        # TODO fix rank calculation this is not correct
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
    def eigen_values(self) -> Vector:
        # TODO implement eigen value calculation
        pass

    @property
    def jordan_form(self) -> Matrix:
        # TODO implement jordan form calculation
        pass

    @property
    def chain_basis(self) -> list[Vector]:
        # TODO implement chain basis calculation
        pass

    # @property
    # def characteristic_polynomial(self) -> SimplePolynomial.SimplePolynomial:
    #     # TODO implement characteristic polynomial calculation
    #     pass

    # @property
    # def minimal_polynomial(self) -> SimplePolynomial.SimplePolynomial:
    #     # TODO implement minimal polynomial calculation
    #     pass

    def __getitem__(self, index: int) -> Any:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        return self.__matrix[index]

    def __setitem__(self, index: int, value: list[Any]) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not isinstance(value, list):
            raise TypeError("Value must be a list")
        if not 0 <= index < self.__rows:
            raise ValueError("Index out of range")
        # TODO validate all items in list are of same type of this matrix
        self.__matrix[index] = value

    def __str__(self, turnc: int = 2) -> str:
        def find_spaceing():
            res = 0
            for row in self:
                for v in row:
                    if hasattr(v, '__round__'):
                        if almost_equal(round(v), v):
                            v = round(v)
                    res = max(res, len(str(v)))
            return res
        spacing = find_spaceing()+2
        n = len(self[0])
        vl = "|"
        hl = (1+spacing)*n*"-" + "\n"
        result = hl
        for i, row in enumerate(self.__matrix):
            result += vl
            for v in row:
                if hasattr(v, '__round__'):
                    if almost_equal(round(v), v):
                        v = round(v)
                result += str(v).center(spacing)+vl
            result += "\n"+hl
            # result += " | "+str(self.__solution_vector[i]) + "\n"
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

    def __mul__(self, other: Union[float, Complex, Vector, Matrix]) -> Union[float, Complex, Vector, Matrix]:
        """
        self * other
        """
        from ..la2 import Calculable
        if isoneof(other, [int, float, Complex, Calculable]):
            res: list[list[Any]] = []
            # res = self
            for i in range(len(self)):
                res.append([])
                for j in range(len(self[0])):
                    res[i].append(self[i][j] * other)
            return Matrix(res)
            # return Matrix([[other * self.__matrix[i][j] for j in range(len[self[0]])]
            #                for i in range(len(self))])
        if isinstance(other, Vector):
            if self.__cols != other.length:
                raise ValueError(
                    "Matrix and Vector must have the same number of rows")
            return Vector([sum([self.__matrix[i][j] * other[j] for j in range(self.__cols)])
                           for i in range(self.__rows)])
        if isinstance(other, Matrix):
            if self.__cols != other.__rows:
                raise ValueError(
                    "Matrix and Matrix must have matching sizes: self.cols == other.rows")
            return Matrix([[sum([self.__matrix[i][j] * other.__matrix[j][k] for j in range(self.__cols)])
                            for k in range(other.__cols)] for i in range(self.__rows)])

        raise TypeError(
            "Matrix can only be multiplied by a number, Vector, or Matrix")

    def __rmul__(self, other: Union[int, float, Complex, Vector, Matrix]) -> Union[float, Complex, Vector, Matrix]:
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
        res: list[list[Any]] = []
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

    def apply_operation(self, operation: MatrixOperationType, iv1, iv2, operate_with=None) -> Matrix:
        if not isinstance(operation, MatrixOperationType):
            raise TypeError("can only apply MatrixOperationType")
        match(operation):
            case MOT.ROW_MULTIPLICATION:
                self[iv1] = [iv2*v for v in self[iv1]]
            case MOT.ROW_ADDITION:
                self[iv1] = [self[iv1][i]+self[iv2][i]
                             for i in range(len(self[iv1]))]
            case MOT.ROW_SWITCHING:
                self[iv1], self[iv2] = self[iv2], self[iv1]
            case MOT.COL_SWITCHING:
                for i in range(len(self[0])):
                    self[i][iv1], self[i][iv2] = self[i][iv2], self[i][iv1]
            case MOT.COL_MULTIPLICATION:
                for i in range(len(self[0])):
                    self[i][iv1] *= iv2
            case MOT.COL_ADDITION:
                for i in range(len(self[0])):
                    self[i][iv1] += self[i][iv2]
        return operate_with

    def concat(self, other) -> Matrix:
        if not isoneof(other, [Vector, Matrix]):
            raise TypeError("can only concat with a Vector or Matrix")
        if len(other) != len(self):
            raise TypeError(
                "can only concat with a Matrix|Vector with the same number of rows")
        if isinstance(other, Vector):
            other = Matrix.fromVector(other)
        res = []
        for i in range(len(self)):
            res.append(self[i] + other[i])
        return Matrix(res)

    def split(self, index: int) -> Tuple[Matrix, Matrix]:
        if not isinstance(index, int):
            raise TypeError("can only split at an int")
        if not 0 <= index <= len(self[0]):
            raise ValueError("index out of range")
        if index == len(self[0]):
            return self, None
        return Matrix([[self[i][j] for j in range(index)] for i in range(len(self))], self.field), Matrix([[self[i][j] for j in range(index, len(self[0]))] for i in range(len(self))], self.field)

    def guassian_elimination(self, solve_with: Union[Vector, Matrix] = None) -> Tuple[Matrix, Union[None, Matrix]]:
        SPLIT_INDEX = len(self[0])
        res = self
        if solve_with is not None:
            if not (isoneof(solve_with, [Vector, Matrix]) or solve_with is None):
                raise TypeError("can only solve with a Vector or Matrix")
            res = self.concat(solve_with)
        # reorder rows
        res.reorgenize_rows()
        # performe gaussian elimination
        for curr_row_index in range(len(res)):
            # find lead value for current row
            for lead_index in range(curr_row_index, SPLIT_INDEX):
                if res[curr_row_index][lead_index] != 0:
                    break
            else:
                break
            lead_value = res[curr_row_index][lead_index]
            # make lead value equal one and change row acordingly
            if lead_value != 1:
                res.apply_operation(MOT.ROW_MULTIPLICATION,
                                    curr_row_index, 1/lead_value)
            for next_row_index in range(len(res)):
                # skip current row
                if next_row_index == curr_row_index:
                    continue
                # find if need to operate
                for next_row_lead_index in range(lead_index, SPLIT_INDEX):
                    if res[next_row_index][next_row_lead_index] != 0:
                        break
                else:
                    continue
                if next_row_lead_index == lead_index:
                    row_multiplyer = res[next_row_index][next_row_lead_index]
                    res.apply_operation(
                        MOT.ROW_MULTIPLICATION, next_row_index, -1/row_multiplyer)
                    res.apply_operation(
                        MOT.ROW_ADDITION, next_row_index, curr_row_index)
                    res.apply_operation(
                        MOT.ROW_MULTIPLICATION, next_row_index, -row_multiplyer)
        return res.split(SPLIT_INDEX)

    def vectorize(self) -> Vector:
        arr = []
        for col in range(len(self[0])):
            arr += [self[row][col] for row in range(len(self))]
        return Vector(arr)

    def solve(self, vec: Vector) -> Union[Vector, list[Vector], None]:
        """
        Solve the system of equations
        """
        if self.__rows != self.__cols:
            raise ValueError("Matrix must be square")
        if not isinstance(vec, Vector):
            raise TypeError("Matrix must be solved for a vector")
        result_matrix, sol = self.guassian_elimination(vec)
        sol = sol.vectorize()
        # if rank of matrix is equal to number of rows and cols return solution vector
        if result_matrix.rank == len(result_matrix):
            return sol
        # if there is a row in result matrix which has all zeros and solution vector doesnt has a zero at that row there is no solution
        for i, row in enumerate(result_matrix):
            if (not Vector(row).has_no_zero) and sol[i] != 0:
                return None
        # otherwise there is a span of solutions
        # TODO implement solutions for nullity rank > 1
        raise NotImplementedError(
            "nullity rank was atleast 1, not yet implemented")

    def get_eigen_vectors_of(eigenvalue) -> list[Vector]:
        # TODO calculate the eigen space of an eigen value
        pass

    def algebraic_multiplicity(eigenvalue) -> int:
        # TODO calculate the algebraic multiplicity of an eigenvalue
        pass

    def geometric_multiplicity(eigenvalue) -> int:
        # TODO calculate the geometric multiplicity of an eigenvalue
        pass

    # def guassian_elimination(self, sol=None) -> Matrix:
    #     if not sol:
    #         sol = self.__solution_vector

    #     def first_not_zero_index(row: list[float]) -> int:
    #         for i in range(len(row)):
    #             if row[i] != 0:
    #                 break
    #         return i
    #     res = copy.deepcopy(self)
    #     res.__solution_vector = sol
    #     res.reorgenize_rows()
    #     # gaussian elimination
    #     for r in range(res.__rows):
    #         lead_index = first_not_zero_index(res[r])
    #         lead_value = res[r][lead_index]
    #         if lead_value == 0:
    #             continue
    #         if lead_value != 1:
    #             for c in range(res.__cols):
    #                 res[r][c] *= 1/lead_value
    #             res.__solution_vector[r] *= 1/lead_value
    #             lead_value = res[r][lead_index]
    #         for r2 in range(res.__rows):
    #             if r == r2:
    #                 continue
    #             row_divider = res[r2][lead_index]/lead_value
    #             if row_divider == 0:
    #                 continue
    #             for c in range(res.__cols):
    #                 res[r2][c] -= row_divider * res[r][c]
    #             res.__solution_vector[r2] -= row_divider * \
    #                 res.__solution_vector[r]
    #     return res
