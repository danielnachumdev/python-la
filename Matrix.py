from __future__ import annotations
from typing import Any, Union
from Complex import Complex
from Vector import Vector
import copy
import functools


class Matrix:
    def __init__(self, mat: list[list[Union[float, Complex]]], sol_vec: list[Union[float, Complex]] = None) -> None:
        self.matrix = mat
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.solution_vector = sol_vec if sol_vec else [
            0 for _ in range(self.rows)]

    @property
    def rank(self) -> int:
        self.reorgenize_rows()
        rank = 0
        for row in self.matrix:
            if all([i == 0 for i in row]):
                continue
            rank += 1
        return rank

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        return self.matrix[index]

    def __str__(self) -> str:
        result = ""
        for i, row in enumerate(self.matrix):
            result += str(row)
            result += " | "+str(self.solution_vector[i]) + "\n"
        return result

    def __add__(self, other: Matrix) -> Matrix:
        if not Matrix.isInstance(other):
            raise TypeError("Matrix can only be added to another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
                       for i in range(self.rows)])

    def __neg__(self) -> Matrix:
        return Matrix([[-self.matrix[i][j] for j in range(self.cols)]
                       for i in range(self.rows)])

    def transpose(self) -> Matrix:
        return Matrix([[self.matrix[j][i] for j in range(self.cols)]
                       for i in range(self.rows)])

    def __sub__(self, other: Matrix) -> Matrix:
        if not Matrix.isInstance(other):
            raise TypeError(
                "Matrix can only be subtracted from another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
                       for i in range(self.rows)])

    def __mul__(self, other: Union[float, Complex, Vector, Matrix]) -> Union[float, Complex, Vector, Matrix]:
        """
        self * other
        """
        if isinstance(other, float) or isinstance(other, Complex) or isinstance(other, int):
            return Matrix([[other * self.matrix[i][j] for j in range(self.cols)]
                           for i in range(self.rows)])
        if isinstance(other, Vector):
            if self.cols != other.length:
                raise ValueError(
                    "Matrix and Vector must have the same number of rows")
            return Vector([sum([self.matrix[i][j] * other[j] for j in range(self.cols)])
                           for i in range(self.rows)])
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    "Matrix and Matrix must have matching sizes: self.cols == other.rows")
            return Matrix([[sum([self.matrix[i][j] * other.matrix[j][k] for j in range(self.cols)])
                            for k in range(other.cols)] for i in range(self.rows)])
        raise TypeError(
            "Matrix can only be multiplied by a number, Vector, or Matrix")

    def __rmul__(self, other: Union[int, float, Complex, Vector, Matrix]) -> Union[float, Complex, Vector, Matrix]:
        """
        other * self
        """
        if isinstance(other, float) or isinstance(other, Complex) or isinstance(other, int):
            return self.__mul__(other)
        if isinstance(other, Vector):
            raise TypeError(
                "Matrix can only be multiplied by a vector from the right")
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    "Matrix and Matrix must have the same number of columns")
            return Matrix([[sum([self.matrix[i][j] * other.matrix[j][k] for j in range(self.cols)])
                            for k in range(other.cols)] for i in range(self.rows)])
        raise TypeError(
            "Matrix can only be multiplied by a number, Vector, or Matrix")

    def __eq__(self, other: Matrix) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError("Matrix can only be compared to another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            return False
        if any([self.matrix[i][j] != other.matrix[i][j] for i in range(self.rows) for j in range(self.cols)]):
            return False
        return True

    def reorgenize_rows(self):
        def comparer(a: list[float], b: list[float]) -> bool:
            def first_not_zero_index(row: list[float]) -> int:
                for i in range(len(row)):
                    if row[i] != 0:
                        break
                return i
            return -1 if first_not_zero_index(a) > first_not_zero_index(b) else 1
        self.matrix = sorted(
            self.matrix, key=functools.cmp_to_key(comparer), reverse=True)

    def solve(self) -> Matrix:
        """
        Solve the system of equations
        """
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
        # if self.rows != self.solution_vector.length:
        #     raise ValueError(
        #         "Matrix and solution vector must have the same number of rows")

        def first_not_zero_index(row: list[float]) -> int:
            for i in range(len(row)):
                if row[i] != 0:
                    break
            return i
        res = copy.deepcopy(self)
        res.reorgenize_rows()
        for r in range(res.rows):
            lead_index = first_not_zero_index(res[r])
            lead_value = res[r][lead_index]
            if lead_value == 0:
                continue
            if lead_value != 1:
                for c in range(res.cols):
                    res[r][c] /= lead_value
                res.solution_vector[r] /= lead_value
                lead_value = res[r][lead_index]
            for r2 in range(res.rows):
                if r == r2:
                    continue
                row_divider = res[r2][lead_index]/lead_value
                if row_divider == 0:
                    continue
                for c in range(res.cols):
                    res[r2][c] -= row_divider * res[r][c]
                res.solution_vector[r2] -= row_divider * \
                    res.solution_vector[r]
        if res.rank != res.rows:
            return "nullity rank was atleast 1, not yet implemented"  # TODO

        return res

    @staticmethod
    def fromVector(vec: Vector) -> Matrix:
        return Matrix([[vec.__values[i] for i in range(vec.get_length())]])

    @staticmethod
    def fromString(matrix_string: str) -> Matrix:
        return Matrix([[int(num) for num in row.split()]
                       for row in matrix_string.split("\n")])

    @staticmethod
    def isInstance(val: Any) -> bool:
        return isinstance(val, Matrix)
