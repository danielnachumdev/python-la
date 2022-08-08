from __future__ import annotations
from typing import Any, Union
import enum
import copy
import functools
from typing import Tuple
from ..utils import almost_equal
from .Complex import Complex
from .Vector import Vector
from .Field import Field, RealField
from ..utils import areinstances, check_foreach, isoneof
from .Span import Span


class MatrixOperationType(enum.Enum):
    ROW_SWITCHING = "row_switching"
    ROW_MULTIPLICATION = "row_multiplication"
    ROW_ADDITION = "row_addition"
    COL_SWITCHING = "column_switching"
    COL_MULTIPLICATION = "column_multiplication"
    COL_ADDITION = "column_addition"


MOT = MatrixOperationType


class Matrix:

    @staticmethod
    def fromVector(vec: Vector) -> Matrix:
        """Create a Matrix from a single Vector, the matrix will have 1 column and the same number of rows as the vector

        Args:
            vec (Vector): the vector to create a mtrix from

        Raises:
            TypeError: wiil rise if vec is not a Vector

        Returns:
            Matrix: the result
        """
        if not isinstance(vec, Vector):
            raise TypeError("Vector must be a Vector")
        return Matrix([[v] for v in vec], vec.field)

    @staticmethod
    def from_vectors(vecs: list[Vector]) -> Matrix:
        """Create a Matrix from a list of Vectors, the matrix will have the same number of columns as the number of vectors and the same number of rows as the number of elements in a vector

        Args:
            vecs (list[Vector]): the list of vector to create a matrix from

        Raises:
            TypeError: will rise if vecs is not a list of Vectors
            ValueError: will rise if vecs are not over the same field

        Returns:
            Matrix: the result
        """
        if not areinstances(vecs, Vector):
            raise TypeError("all elements must be instances of class 'Vector'")
        if not check_foreach(vecs, lambda v: v.field == vecs[0].field):
            raise ValueError("vectors are not over the same field")
        mat: list[list[Any]] = []
        for i in range(len(vecs[0])):
            mat.append([])
            for j in range(len(vecs)):
                mat[i].append(vecs[j][i])
        return Matrix(mat, field=vecs[0].field)

    # @staticmethod
    # def fromString(matrix_string: str) -> Matrix:
    #     """Create a Matrix from a string representation of a matrix

    #     Args:
    #         matrix_string (str): the sr

    #     Returns:
    #         Matrix: _description_
    #     """
    #     return Matrix([[int(num) for num in row.split()]
    #                    for row in matrix_string.split("\n")])

    @staticmethod
    def random(rows: int, cols: int, f: Field = RealField(), min: float = -10, max: float = 10, ) -> Matrix:
        """Create a random Matrux acording to params

        Args:
            rows (int): the amount of rows in matrix
            cols (int): the amount of columns in matrix
            f (Field, optional): the field to create the matrix over. Defaults to RealField().
            min (float, optional): the minimum value from the field. Defaults to -10.
            max (float, optional): the maximum value from the field. Defaults to 10.

        Returns:
            Matrix: the result
        """

        return Matrix([[f.random(min, max) for _ in range(cols)]for __ in range(rows)], field=f)

    @staticmethod
    def from_jordan_blocks(blocks: list[Matrix]) -> Matrix:
        """Create a Matrix from a list of Jordan blocks

        Args:
            blocks (list[Matrix]): the list of Jordan blocks to create a matrix from

        Returns:
            Matrix: the result
        """
        total_size = 0
        hm: dict[Any, list[Matrix]] = dict()
        for block in blocks:
            if block[0][0] not in hm.keys():
                hm[block[0][0]] = []
            hm[block[0][0]].append(block)
            total_size += len(block)
        # sort blocks in order
        for key in hm:
            hm[key].sort(key=lambda x: len(x))
        res = Matrix([[0 for __ in range(total_size)] for _ in range(total_size)],
                     field=blocks[0].field)
        offset = 0
        for key in hm:
            for block in hm[key]:
                for i, row in enumerate(block):
                    for j, v in enumerate(row):
                        res[i + offset][j + offset] = v
                offset += len(block)
        return res

    @staticmethod
    def create_jordan_blcok(size: int, eigenvalue: Any) -> Matrix:
        """Create a Jordan block from a size and an eigenvalue

        Args:
            size (int): the size of the block
            eigenvalue (Any): the eigenvalue of the block

        Returns:
            Matrix: the result
        """
        m = Matrix.identity(size)-Matrix.identity(size)
        for i in range(size-1):
            m[i+1][i] = 1
        return Matrix.identity(size)*eigenvalue + m

    @staticmethod
    def identity(size: int) -> Matrix:
        """Create identity matrix if given size

        Args:
            size (int): the size of the matrix

        Returns:
            Matrix: the result
        """
        arr = [[0 for __ in range(size)] for _ in range(size)]
        for i in range(size):
            arr[i][i] = 1
        return Matrix(arr)

    def __init__(self, mat: list[list[Any]], field: Field = RealField()) -> None:
        """Create a Matrix

        Args:
            mat (list[list[Any]]): a list of lists of elements (2D array)
            field (Field, optional): the field that the elements of the matrix is over. Defaults to RealField().

        Raises:
            TypeError: will rise if mat is not a list of lists
        """
        if not isinstance(mat, list) or not all([isinstance(v, list) for v in mat]):
            raise TypeError("Matrix must be a 2d array")
        self.__matrix = mat
        self.__rows = len(mat)
        self.__cols = len(mat[0])
        self.field = field

    @property
    def kernel(self) -> Union[Vector, Span]:
        """Get the kernel of the matrix

        Returns:
            Union[Vector, Span]: the result
        """
        solution = self.solve(Vector.from_size(len(self), self.field))
        if solution is None:
            return Vector([0 for _ in range(len(self))])
        return solution

    @property
    def image(self) -> list[Vector]:
        """Get the image of the matrix

        Returns:
            list[Vector]: the result
        """
        from .VectorSpace import VectorSpace
        return VectorSpace(self.field).standard_basis() - self.kernel

    @property
    def rank(self) -> int:
        """Get the rank of the matrix

        Returns:
            int: the result
        """
        # TODO fix rank calculation this is not correct
        tmp = self.gaussian_elimination()
        rank = 0
        for i in range(min(len(tmp), len(tmp[0]))):
            for v in tmp[i]:
                if v != tmp.field.zero:
                    rank += 1
                    break

        # for i in tmp.__matrix:
        #     if not all([i == 0 for i in i]):
        #         rank += 1
        return rank

    @property
    def determinant(self) -> Any:
        """Calculate the determinant of the matrix

        Raises:
            ValueError: will rise if the matrix is not square

        Returns:
            Any: the result
        """
        if self.__rows != self.__cols:
            raise ValueError("Matrix must be square")
        if self.__rows == 1:
            return self.__matrix[0][0]
        if self.__rows == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]
        return sum([self.__matrix[i][0] * ((-1)**i) * self.minor(i, 0) for i in range(self.__rows)])

    @property
    def is_invertiable(self) -> bool:
        """returns wheter the matrix is invertible

        Returns:
            bool: True if the matrix is invertible, False otherwise
        """
        return self.determinant != 0

    @property
    def is_square(self) -> bool:
        """returns wheter the matrix is square

        Returns:
            bool: True if the matrix is square, False otherwise
        """
        return self.__rows == self.__cols

    @property
    def is_symmetrical(self) -> bool:
        """returns wheter the matrix is symmetrical

        Returns:
            bool: True if the matrix is symmetrical, False otherwise
        """
        if not self.is_square:
            return False
        for i in range(len(self)):
            for j in range(i, len(self)):
                if self[i][j] != self[j][i]:
                    return False
        return True

    @property
    def is_asymmetrical(self) -> bool:
        """returns wheter the matrix is asymmetrical

        Returns:
            bool: True if the matrix is asymmetrical, False otherwise
        """
        if not self.is_square:
            return False
        for i in range(len(self)):
            for j in range(i, len(self)):
                if self[i][j] != -self[j][i]:
                    return False
        return True

    @property
    def conjugate_transpose(self) -> Matrix:
        return self.transpose().conjugate()

    @property
    def is_diagonialable(self) -> bool:
        """returns wheter the matrix is diagonialable

        Returns:
            bool: True if the matrix is diagonialable, False otherwise
        """
        for eigenvalue in set(self.eigenvalues):
            if not (self.algebraic_multiplicity(eigenvalue) == self.geometric_multiplicity(eigenvalue)):
                return False
        return True

    @property
    def is_nilpotent(self) -> bool:
        # TODO implement nilpotency check
        pass

    @property
    def eigenvalues(self) -> list[Any]:
        """Get the eigenvalues of the matrix

        Returns:
            list: the result
        """
        return self.characteristic_polynomial.roots

    @property
    def jordan_form(self) -> Matrix:
        """Get the Jordan form of the matrix

        Raises:
            ValueError: will rise if the matrix is not square

        Returns:
            Matrix: the result
        """
        if not self.is_square:
            raise ValueError("Matrix must be square")
        blocks = []
        eigenvalues = self.eigenvalues
        for eigenvalue in set(eigenvalues):
            geom = self.geometric_multiplicity(eigenvalue)
            alge = eigenvalues.count(eigenvalue)
            if geom == 1:
                blocks.append(self.create_jordan_blcok(alge, eigenvalue))
            elif geom == alge:
                blocks.append(eigenvalue*Matrix.identity(alge))
            else:
                # alge>geom => chain_basis
                pass
        return Matrix.from_jordan_blocks(blocks)

    @property
    def chain_basis(self) -> list[Vector]:
        # TODO implement chain basis calculation
        pass

    @property
    def characteristic_polynomial(self):
        """Get the characteristic polynomial of the matrix

        Raises:
            ValueError: will rise if the matrix is not square

        Returns:
            PolynomialSimple: the result
        """
        from ..la2 import PolynomialSimple
        if not self.is_square:
            raise ValueError("Matrix must be square")
        return (Matrix.identity(len(self))*PolynomialSimple([1], [1])-self).determinant

    @property
    def minimal_polynomial(self):
        """Get the minimal polynomial of the matrix

        Returns:
            _type_: the result
        """
        from ..la2 import PolynomialSimple
        res = PolynomialSimple([1], [0])
        for eigenvalue in set(self.eigenvalues):
            res *= PolynomialSimple([1, -eigenvalue], [1, 0]
                                    )**self.geometric_multiplicity(eigenvalue)
        return res

    def __getitem__(self, index: int) -> list[Any]:
        """wil return the row at the given index

        Args:
            index (int): the index of desire row

        Raises:
            TypeError: will rise if index is not an int
            ValueError: will rise if index is out of range

        Returns:
            list[Any]: the row at the given index
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not (0 <= index <= self.__rows):
            raise ValueError("Index out of range")
        return self.__matrix[index]

    def __setitem__(self, index: int, value: list[Any]) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if not 0 <= index < self.__rows:
            raise ValueError("Index out of range")
        if not isinstance(value, list):
            raise TypeError("Value must be a list")
        # FIXME validate all items in list are of same type of this matrix
        self.__matrix[index] = value

    def __str__(self, turnc: int = 2) -> str:
        """will return a string representation of the matrix

        Args:
            turnc (int, optional): how many digist to turnicate. Defaults to 2.

        Returns:
            str: the srtring representation
        """
        def round_if_possible(v):
            if hasattr(v, '__round__'):
                if almost_equal(round(v), v):
                    v = round(v)
            return v

        def turnacate(v):
            v = str(v)
            return v[:v.index(".")+1+turnc] if "." in v else v

        def find_spaceing():
            res = 0
            for row in self:
                for v in row:
                    v = round_if_possible(v)
                    v = turnacate(v)
                    res = max(res, len(str(v)))
            return res
        spacing = find_spaceing()+2
        n = len(self[0])
        vl = "|"
        hl = (1+spacing)*n*"-" + "-" + "\n"
        result = hl
        for i, row in enumerate(self.__matrix):
            result += vl
            for v in row:
                v = round_if_possible(v)
                v = turnacate(v)
                result += str(v).center(spacing)+vl
            result += "\n"+hl
        return result

    def __add__(self, other: Matrix) -> Matrix:
        """will add two matrices together and return the result

        Args:
            other (Matrix): the matrix to add to current one

        Raises:
            TypeError: will rise if other is not a matrix
            ValueError: will rise if the matrices are not of the same size

        Returns:
            Matrix: the result matrix
        """
        if not isinstance(other, Matrix):
            raise TypeError("Matrix can only be added to another Matrix")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.__matrix[i][j] + other.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __neg__(self) -> Matrix:
        """will return the negative of the matrix

        Returns:
            Matrix: the negative matrix
        """
        return Matrix([[-self.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __sub__(self, other: Matrix) -> Matrix:
        """will subtract two matrices and return the result

        Args:
            other (Matrix): the matrix to subtract from current one

        Raises:
            TypeError: will rise if other is not a matrix
            ValueError: will rise if the matrices are not of the same size

        Returns:
            Matrix: the result matrix
        """
        if not isinstance(other, Matrix):
            raise TypeError(
                "Matrix can only be subtracted from another Matrix")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.__matrix[i][j] - other.__matrix[i][j] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def __mul__(self, other: Any) -> Any:
        """will multiply the matrix with the given value and return the result

        Args:
            other (Union[int, float, Complex, Vector, Matrix, Calculable]): the value to multiply with

        Raises:
            ValueError: will rise if the value is not one of the above types

        Returns:
            Any: [int, float, Complex, Vector, Matrix, Calculable]
        """
        from ..la2 import Calculable
        if not isoneof(other, [int, float, complex, Vector, Matrix, Calculable]):
            raise ValueError(
                "Can only multiply with a int, float, complex, Vector, Matrix or Calculable")
        if isoneof(other, [int, float, Complex, Calculable]):
            res: list[list[Any]] = []
            for i in range(len(self)):
                res.append([])
                for j in range(len(self[0])):
                    res[i].append(self[i][j] * other)
            return Matrix(res)
        if isinstance(other, Vector):
            if self.__cols != len(other):
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

    def __rmul__(self, other: Union[int, float, Complex, Vector, Matrix]) -> Union[float, Complex, Vector, Matrix]:
        """will multiply the matrix with the given value and return the result

        Args:
            other (Union[int, float, Complex, Vector, Matrix, Calculable]): the value to multiply with

        Raises:
            ValueError: will rise if the value is not one of the above types

        Returns:
            Any: [int, float, Complex, Vector, Matrix, Calculable]
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

    def __eq__(self, other: Matrix, use_almost_equale: bool = True) -> bool:
        """will compare two matrices and return True if they are equal

        Args:
            other (Matrix): the other matrix to compare to
            use_almost_equale (bool, optional): Specifies wheter to use almost_equal when comparing Matricies. Defaults to True.

        Raises:
            TypeError: will rise it the other object is not a Matrix
            TypeError: wiil rise if use_almost_equale is not a bool

        Returns:
            bool: True if the objects are equal, False otherwise
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"cant complare 'Matrix' with '{type(other)}'")
        if not isinstance(use_almost_equale, bool):
            raise TypeError("use_almost_equale must be a boolean")
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return False
        if use_almost_equale:
            return all([all([almost_equal(self[i][j], other[i][j])] for j in range(len(self[0]))) for i in range(len(self))])
        if any([self.__matrix[i][j] != other.__matrix[i][j] for i in range(self.__rows) for j in range(self.__cols)]):
            return False
        return True

    def __ne__(self, other: Matrix, use_almost_equale: bool = True) -> bool:
        """will compare two matrices and return True if they are not equal

        Args:
            other (Matrix): the other matrix to compare to
            use_almost_equale (bool, optional): Specifies wheter to use almost_equal when comparing Matricies. Defaults to True.

        Raises:
            TypeError: will rise if __eq__ would raise an error

        Returns:
            bool: True if the objects are not equal, False otherwise
        """
        try:
            return not self.__eq__(other, use_almost_equale)
        except TypeError as e:
            raise e

    def __len__(self) -> int:
        """will return the number of rows in the matrix

        Returns:
            int: the number of rows in the matrix
        """
        return self.__rows

    def __pow__(self, value: int) -> Matrix:
        """will raise the matrix to the given power and return the result in a new matrix

        Args:
            value (int): the power to raise the matrix to

        Raises:
            TypeError: will rise if value is not an int
            ValueError: will rise if value is less than 0

        Returns:
            Matrix: the result of the power
        """
        if isinstance(value, float):
            if int(value) != value:
                raise ValueError("value must be an integer")
            value = int(value)
        if not isinstance(value, int):
            raise TypeError("value must be an int")
        if not (0 <= value):
            raise ValueError("value must be atleast than 0")
        res = self
        for _ in range(value-1):
            res *= self
        return res

    def inverse(self) -> Matrix:
        pass
        # if not self.is_invertiable:
        #     raise ValueError("Matrix must be invertible")
        # return Matrix([[self.minor(i, j) / self.determinant for j in range(self.__cols)]
        #                for i in range(self.__rows)])

    def cofactor(self, row_to_ignore: int, col_to_ignore: int) -> Matrix:
        """will return the cofactor of the matrix at the given position

        Args:
            row_to_ignore (int): the row to ignore
            col_to_ignore (int): the column to ignore

        Raises:
            ValueError: will rise if the given row or column is out of range

        Returns:
            Matrix: the cofactor of the matrix at the given position
        """
        if not((0 <= row_to_ignore < self.__rows) and (0 <= col_to_ignore < self.__cols)):
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

    def minor(self, row_to_ignore: int, col_to_ignore: int) -> Any:
        """will return the minor of the matrix at the given position (the determinant of the cofactor)

        Args:
            row_to_ignore (int): the row to ignore
            col_to_ignore (int): the column to ignore

        Raises:
            will rise whatever cofator and/or determinant will raise

        Returns:
            Any: the minor of the matrix at the given position
        """
        return self.cofactor(row_to_ignore, col_to_ignore).determinant

    def transpose(self) -> Matrix:
        """will return the transpose of the matrix

        Returns:
            Matrix: the transpose of the matrix
        """
        return Matrix([[self.__matrix[j][i] for j in range(self.__cols)]
                       for i in range(self.__rows)])

    def conjugate(self) -> Matrix:
        """will return the conjugate of the matrix

        Returns:
            Matrix: the conjugate of the matrix
        """
        arr: list[list[Any]] = []
        for row in self:
            arr.append([])
            for v in row:
                if hasattr(v, "conjugate"):
                    if callable(getattr(v, "conjugate")):
                        arr[-1].append(v.conjugate())
                    arr[-1].append(v.conjugate)
                else:
                    arr[-1].append(v)
        return Matrix(arr, self.field)

    def reorgenize_rows(self) -> None:
        """Reorgenizes the rows of the matrix
        """
        def comparer(a: list[float], b: list[float]) -> bool:
            def first_not_zero_index(row: list[float]) -> int:
                i = 0
                while i < len(row):
                    if row[i] != self.field.zero:
                        break
                    i += 1
                return i

            a_index = first_not_zero_index(a)
            b_index = first_not_zero_index(b)
            if a_index == b_index:
                return 0
            return -1 if a_index > b_index else 1

        self.__matrix = sorted(
            self.__matrix, key=functools.cmp_to_key(comparer), reverse=True)

    def apply_operation(self, operation: MatrixOperationType, iv1, iv2, operate_with=None) -> Matrix:
        if not isinstance(operation, MatrixOperationType):
            raise TypeError("can only apply MatrixOperationType")
        if operation == MOT.ROW_MULTIPLICATION:
            self[iv1] = [iv2*v for v in self[iv1]]
        elif operation == MOT.ROW_ADDITION:
            self[iv1] = [self[iv1][i]+self[iv2][i]
                         for i in range(len(self[iv1]))]
        elif operation == MOT.COL_SWITCHING:
            self[iv1], self[iv2] = self[iv2], self[iv1]
        elif operation == MOT.COL_SWITCHING:
            for i in range(len(self[0])):
                self[i][iv1], self[i][iv2] = self[i][iv2], self[i][iv1]
        elif operation == MOT.COL_MULTIPLICATION:
            for i in range(len(self[0])):
                self[i][iv1] *= iv2
        elif operation == MOT.COL_ADDITION:
            for i in range(len(self[0])):
                self[i][iv1] += self[i][iv2]

        return operate_with

    def concat(self, other: Union[Vector, Matrix]) -> Matrix:
        """will concatenate the matrix with the given matrix and return the result in a new matrix

        Args:
            other (Union[Vector, Matrix]): the matrix/vector to concatenate with

        Raises:
            TypeError: will rise if other is not a Matrix or Vector
            ValueError: will rise if the len(self) != len(other)

        Returns:
            Matrix: the result of the concatenation
        """
        if not isoneof(other, [Vector, Matrix]):
            raise TypeError("can only concat with a Vector or Matrix")
        if len(other) != len(self):
            raise ValueError(
                "can only concat with a Matrix|Vector with the same number of rows")
        if isinstance(other, Vector):
            other = Matrix.fromVector(other)
        res = []
        for i in range(len(self)):
            res.append(self[i] + other[i])
        return Matrix(res)

    def split(self, index: int) -> Tuple[Matrix, Matrix]:
        """will split the matrix into two matrices at the given index

        Args:
            index (int): the index to split the matrix at

        Raises:
            TypeError: will rise if index is not an int
            ValueError: will rise if index is out of range

        Returns:
            Tuple[Matrix, Matrix]: the two matrices resulting from the split
        """
        if not isinstance(index, int):
            raise TypeError("can only split at an int")
        if not 0 <= index <= len(self[0]):
            raise ValueError("index out of range")
        if index == len(self[0]):
            return self, None
        return Matrix([[self[i][j] for j in range(index)] for i in range(len(self))], self.field), Matrix([[self[i][j] for j in range(index, len(self[0]))] for i in range(len(self))], self.field)

    def duplicate(self) -> Matrix:
        mat: list[list[Any]] = []
        for i, row in enumerate(self):
            mat.append([])
            for v in row:
                mat[i].append(v)
        return Matrix(mat, self.field)

    def gaussian_elimination_with(self, solve_with: Union[Vector, Matrix] = None) -> Tuple[Matrix, Union[None, Matrix]]:
        """will perform gaussian elimination on the matrix and return the result in a new matrix and the solution if solve_with is given

        Args:
            solve_with (Union[Vector, Matrix], optional): the vector/matrix to solve with. Defaults to None.

        Raises:
            TypeError: will rise if solve_with is not a Vector or Matrix

        Returns:
            Tuple[Matrix, Union[None, Matrix]]: the result of the gaussian elimination and the solution if solve_with is given
        """
        SPLIT_INDEX = len(self[0])
        res = self.duplicate()
        if solve_with is not None:
            if not (isoneof(solve_with, [Vector, Matrix]) or solve_with is None):
                raise TypeError("can only solve with a Vector or Matrix")
            res = self.concat(solve_with)
        # reorder rows
        res.reorgenize_rows()
        # performe gaussian elimination
        for curr_row_index in range(len(res)):
            # find lead value for current row
            for lead_index in range(SPLIT_INDEX):
                if res[curr_row_index][lead_index] != 0:
                    break
            else:
                continue
            # else:
            #     break
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
        res.reorgenize_rows()
        return res.split(SPLIT_INDEX)

    def gaussian_elimination(self) -> Matrix:
        """will perform gaussian elimination on the matrix and return the result in a new matrix

        Returns:
            Matrix: the result of the gaussian elimination
        """
        return self.gaussian_elimination_with(None)[0]

    def vectorize(self) -> Vector:
        """will vectorize the matrix columns first and return the result in a new vector

        Returns:
            Vector: the result of the vectorization
        """
        arr = []
        for col in range(len(self[0])):
            arr += [self[row][col] for row in range(len(self))]
        return Vector(arr)

    def solve(self, vec: Vector) -> Union[None, Vector, Span]:
        """will solve the matrix with the given vector and return the solution

        Args:
            vec (Vector): the vector to solve with

        Raises:
            TypeError: will rise if vec is not a Vector
            NotImplementedError: will rise if there is a span of solutions and vector!=V0 ,WILL BE IMPLEMENTED LATER

        Returns:
            None: if there is no solution
            Vector: if there is a single solution
            Span: if there are multiple solutions
        """
        if not isinstance(vec, Vector):
            raise TypeError("Matrix must be solved for a vector")
        result_matrix, sol = self.gaussian_elimination_with(vec)
        sol = sol.vectorize()

        # if rank of matrix is equal to number of rows and cols return solution vector
        if result_matrix.rank == len(result_matrix) == len(result_matrix[0]):
            return sol

        # if there is a row in result matrix which has all zeros and solution vector doesnt has a zero at that row there is no solution
        for i, row in enumerate(result_matrix):
            # if (not Vector(row).has_no_zero) and sol[i] != 0:
            #     return None
            has_no_zero = check_foreach(row, lambda x: x != 0)
            if has_no_zero and sol[i] != 0:
                return None
        # otherwise there is a span of solutions

        # solve for V0
        def get_solutions_from_columns(m: Matrix) -> list[Vector]:
            def sumrows(m: Matrix) -> list[int]:
                sumrow = [0 for _ in range(len(m[0]))]
                for i in range(m.rank):
                    row = m[i]
                    for j, v in enumerate(row):
                        if v != m.field.zero:
                            sumrow[j] += 1
                return sumrow
            res = []
            for i2, v in enumerate(sumrows(m)):
                if v == m.field.zero:
                    res.append(Vector.e(i2, len(m), m.field))
            return res

        def get_solutions_from_rows(m: Matrix) -> list[Vector]:
            res = []
            value_depends_on_key: dict[int, set] = dict()
            free_cofactors = [0 for _ in range(len(m[0]))]
            for row_index in range(m.rank):
                row = m[row_index]
                for candidate_index, candidate in enumerate(row):
                    if candidate != m.field.zero:
                        for validator_index in range(candidate_index+1, len(row)):
                            if row[validator_index] != m.field.zero:
                                if validator_index not in value_depends_on_key:
                                    value_depends_on_key[validator_index] = set(
                                    )
                                    free_cofactors[validator_index] = row[validator_index]
                                value_depends_on_key[validator_index].add(
                                    candidate_index)
                        break
            CANDIDATE_INDEX_INDEX = 0
            ROW_INDEX_INDEX = 1
            for key in value_depends_on_key:
                tmp = [0 for _ in range(len(m[0]))]
                tmp[key] = m.field.one
                for index in value_depends_on_key[key]:
                    tmp[index] = -free_cofactors[key]  # m.field.one
                res.append(Vector(tmp))
            return res
        solution_span_as_arr = get_solutions_from_columns(
            result_matrix)+get_solutions_from_rows(result_matrix)
        if len(solution_span_as_arr) == 0:
            return sol
        return Span(solution_span_as_arr, sol)

    def get_eigen_vectors_of(self, eigenvalue) -> list[Vector]:
        # assume that the matrix is square
        m: Matrix = self-eigenvalue*Matrix.identity(len(self))
        m **= self.algebraic_multiplicity(eigenvalue)
        return m.kernel

    def algebraic_multiplicity(self, eigenvalue) -> int:
        return self.eigenvalues.count(eigenvalue)

    def geometric_multiplicity(self, eigenvalue) -> int:
        m: Matrix = self-eigenvalue*Matrix.identity(len(self))
        return m.kernel.dim
