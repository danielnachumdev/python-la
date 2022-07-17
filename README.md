
# linear-algebra

  

## Field

* Implemented field axioms checking

* Implemented generic class `Field`

* each instance contains info about the degree of the field and the modulus of the field

* a `random()` function that generates a vector acording to a virtual function which is implemented in the subclasses to generate one element

* Implemented generic subclass for rationals `RationalField`

* Implemented generic subclass for reals `RealField`

* Implemented generic subclass for complex numbers `ComplexField`

* created instances for those subclasses of `degree=1` and `modulus=1` called `DefaultRationalField`, `DefaultRealField`, `DefaultComplexField`

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

* addition, subtraction, negation

* scalar multiplication and division

* dot product

## Span

Partially implemented

## Matrix

Partially implemented

## Linear Transformation

Partially implemented

  
## Calculable
An interface for the following subclasses:
### Polynomial
* #### SimplePolynomial
	An object which represents: `a_n*x^b_n + ... + a_1*x + a_0`
	*  [x] addition, subtraction, negation, multiplication, power
	 * [x] division by scalar
	 * [x]  variable substitution with :
		 *  int
		 * float
		 * Complex
		 * Polynomial
		 * Linear Transformation
		 * Matrix


* #### PolinomialFraction
	An object which represents: `SimplePolynomial1 / SimplePolynomial2`
a superset of SimplePolynomial to add the ability of division  

## Expression - TBD

polinomials, exponents, trigonemtry, logarithm, constants, variables

## InnerProduct

Partially implemented

* Implemented `StandardInnerProduct`

* Implemented `isInnerProduct` that checks if the given function is an inner product (the result is not with absolute certinaty. e.g: if you get a false value it is certianly not an inner product but a true value not neccessearly indicates it is)