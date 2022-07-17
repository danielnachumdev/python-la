
# linear-algebra

  

## Field
__Static methods:__
```python
create
is_field
```
__Private methods:__
```python
__str__
__eq__ virtual
__contains__ virtual

_generate_one virtual
random
```
__Properties:__
```python
classOfInstance
```
__Other classes:__
```python
class  RationalField(Field)
class  RealField(Field)
class  ComplexField(Field)
class  MatrixField(Field)

Fields(Enum)
```
__Instances:__
```python
DefaultRationalField
DefaultRealField
DefaultComplexField
```

## Complex
__Static methods:__
```python
random(min_val: float = -10, max_val: float = 10, value_func=random.randint) -> Complex:
```
__Private methods:__
```python
__add__
__radd__
__sub__
__rsub__
__neg__
__mul__
__rmul__
__truediv__
__rtruediv__
__abs__ := norm
__eq__
__ne__
__pow__
__rpow__ TBD
```
__Properties::__
```python
conjugate
norm
```
## Vector
__Static methods:__
```python
random(min: float = -10, max: float = 10, degree: int = 10, def_value=None, f: Field = Field.DefaultRealField) -> Vector

fromSize(size: int, default_value: Any = 0) -> Vector
```
__Private methods:__
```python
__add__
__radd__
__sub__
__rsub__
__neg__
__mul__
__rmul__
__truediv__
__rtruediv__
__eq__
__ne__
__getitem__
__iter__
__len__

almost_equal
set
norm
dot
toOrthonormal
projection_onto
copy
```
__Properties:__
```python
length
adjoint TBD
has_no_zero
```

## Span
__Static methods:__
```python
spanField(field: Field) -> Span
```
__Private methods:__
```python
__add__
__eq__
__ne__
__getitem__
__iter__
__len__
__contains__

contains
append
toOrthonormal
projection_of
random
is_spanning
```
__Properties:__
```python
dim
basis
has_lineart_dependency
is_orthogonal
is_orthonormal
```

## Matrix
__Static methods:__
```python
fromVector
fromVectors
fromSpan
fromString
random
fromJordanBlocks TBD
createJordanBlcok TBD
id_matrix
```
__Private methods:__
```python
__add__
__sub__
__neg__
__mul__
__rmul__
__truediv__
__rtruediv__
__eq__
__ne__
__getitem__
__len__

almost_equal
inverse
cofactor
minor
tarnspose
reorgenize_rows
guassian_elimination
solve TBD
get_eigen_space_of TBD
algebraic_multiplicity TBD
geometric_multiplicity TBD
```
__Properties:__
```python
kernel TBD
image TBD
rank
determinant
is_invertible
is_square
is_diagonialable TBD
is_nilpotent TBD
eigen_values TBD
jordan_form TBD
chain_basis TBD
characteristic_polynomial TBD
minimal_polynomial TBD
```
Partially implemented

## Linear Transformation
__Static methods:__
```python
isFuncLinearTransformation
fromMatrix
id
```
__Private methods:__
```python
__add__
__radd__
__sub__
__rsub__
__neg__
__mul__
__rmul__
__truediv__
__call__

toMatrix TBD
```
__Properties:__
```python

```
Partially implemented

  
## Calculable
An interface for the following subclasses:
### Polynomial
* #### SimplePolynomial
	__Static methods:__
	```python
	fromString
	```
	__Private methods:__
	```python
	__add__
	__radd__
	__sub__
	__rsub__
	__neg__
	__mul__
	__rmul__
	__truediv__
	__rtruediv__
	__pow__
	__eq__
	__ne__
	__call__
	__len__

	gcd_with TBD
	```
	__Properties:__
	```python
	roots
	degree
	```
* #### PolinomialFraction
	 __Static methods:__
	```python

	```
	__Private methods:__
	```python

	```
	__Properties:__
	```python

	```

### Expression - TBD
__Static methods:__
```python

```
__Private methods:__
```python

```
__Properties:__
```python

```

## InnerProduct

__Static methods:__
```python
isInnerProduct
```
__Private methods:__
```python
__call__
```
__Properties:__
```python

```
__Instances:__
```python
StandardInnerProduct
```