# python-la

Python library for linear algebra with a course-shaped API: vectors, matrices, fields, spans, linear maps, polynomials, and inner-product spaces.

[![PyPI](https://img.shields.io/pypi/v/python-la.svg)](https://pypi.org/project/python-la/)
[![Python](https://img.shields.io/pypi/pyversions/python-la.svg)](https://pypi.org/project/python-la/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Names and operations follow typical first-course linear algebra (`kernel`, `characteristic_polynomial`, `to_orthonormal`, …). It is aimed at readable math-facing code, not high-performance numeric workloads (use NumPy/SciPy for that).

## Install

```bash
pip install python-la
```

Requires Python 3.11+. Runtime dependency: [`danielutils`](https://pypi.org/project/danielutils/).

## Usage

```python
from python_la import Matrix, Span, Vector, PolynomialSimple, LinearMap, RealField, VectorSpace

Matrix([[1, 2], [3, 4]]).gaussian_elimination()
# row-reduced form (identity for this matrix)

Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).characteristic_polynomial
# X^3 - 15X^2 - 18X

Matrix([[1, 0, 1], [0, 1, 1]]).kernel
# span basis vector [-1, -1, 1]

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

Main types: `Matrix`, `Vector`, `Span`, `LinearMap`, `VectorSpace`, field types (`RealField`, and complex/rational variants), polynomials, and (in `la2`) bilinear forms / inner-product spaces.

## Package layout

| Module | Contents |
| ------ | -------- |
| `python_la.la1` | Fields, vectors, matrices, spans, linear maps, vector spaces |
| `python_la.la2` | Polynomials / expressions, bilinear forms, inner products |
| `python_la.utils` | Internal helpers |
| `python_la.other` | Extras (`Graph`, `Permutation`) |

Class-level notes next to the code: [`python_la/la1/README.md`](./python_la/la1/README.md).

## Development

Contributor workflow (layout, tests, PR labels): [`AGENTS.md`](./AGENTS.md).

Report security issues privately via [GitHub advisories](https://github.com/danielnachumdev/python-la/security/advisories/new).

## License

MIT — see [`LICENSE`](./LICENSE).
