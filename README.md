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
Almost fully implemented
* All basic operators
* norm
* conjugate
* static methond for creating random instance
## Vector
Partially implemented
* operations over generic field
## Span
Partially implemented
## Matrix
Partially implemented
## Linear Transformation
Partially implemented
## Polynomial
* addition,subtraction,negation,multiplication,power
* can substitute x for any of the following:
  * inf,float,complex
  * matrix
  * linear transformation
## InnerProduct
Partially implemented
* Implemented `StandardInnerProduct`
* Implemented `isInnerProduct` that checks if the given function is an inner product (the result is not with absolute certinaty. e.g: if you get a false value it is certianly not an inner product but a true value not neccessearly indicates it is)
