# python-la

**Linear algebra in Python that reads like the math** — vectors, matrices, fields, spans, linear maps, polynomials, and inner-product spaces with a small, intentional API.

[![PyPI](https://img.shields.io/pypi/v/python-la.svg)](https://pypi.org/project/python-la/)
[![Python](https://img.shields.io/pypi/pyversions/python-la.svg)](https://pypi.org/project/python-la/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

## Why python-la?

Most numeric stacks optimize for speed and arrays. **python-la** optimizes for **clarity**: Gaussian elimination, kernels, characteristic polynomials, orthonormal bases, and operator polynomials expressed with types that mirror a first linear-algebra course.

- **`Matrix`**, **`Vector`**, **`Span`**, **`LinearMap`**, **`VectorSpace`**
- **Fields** — real, complex, and rational
- **Polynomials** you can compose and apply to maps (`P(lm)(v)`)
- **Bilinear forms** and **inner-product** spaces (`la2`)
- **MIT licensed**, on [PyPI](https://pypi.org/project/python-la/)

## Install

```bash
pip install python-la
```

Runtime dependency: [`danielutils`](https://pypi.org/project/danielutils/).

## Quick start

```python
from python_la import Matrix, Span, Vector, PolynomialSimple, LinearMap, RealField, VectorSpace

Matrix([[1, 2], [3, 4]]).gaussian_elimination()
# identity-like row-reduced form

Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).characteristic_polynomial
# X^3 - 15X^2 - 18X

Matrix([[1, 0, 1], [0, 1, 1]]).kernel
# [-1, -1, 1]

v1, v2 = Vector([3, 4]), Vector([4, 5])
Span([v1, v2]).to_orthonormal()

R2 = RealField(2)
V = VectorSpace(R2)
lm = LinearMap(V, V, lambda vector: Vector([0, vector[0]], R2))
x_squared = PolynomialSimple.from_string("x^2")
plus_1 = PolynomialSimple.from_string("x+1")
P = plus_1(x_squared)  # X^2 + 1
v = V.random()
P(lm)(v) == v
```

## What you get

| Surface | Role |
| -------- | ---- |
| `python_la.la1` | Core LA: fields, vectors, matrices, spans, linear maps, vector spaces |
| `python_la.la2` | Polynomials / expressions, bilinear forms, inner products |
| `python_la.utils` | Helpers and decorators used by the library |
| `python_la.other` | Extras (`Graph`, `Permutation`) |

Deeper class notes live next to the code (for example [`python_la/la1/README.md`](./python_la/la1/README.md)).

## Contributing & development

Agent/developer workflow (layout, tests, PR labels): see [`AGENTS.md`](./AGENTS.md).

Report security issues privately via [GitHub advisories](https://github.com/danielnachumdev/python-la/security/advisories/new) — please do not open a public issue for vulnerabilities.

## License

MIT — see [`LICENSE`](./LICENSE).
