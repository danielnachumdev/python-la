# python-la – Agent Context

Implementation guide for coding agents changing **python-la**. Product pitch and user-facing install: [`README.md`](README.md).

---

## Orientation

| Question | Answer |
| -------- | ------ |
| What is this? | Python **linear algebra** library (course-shaped API: matrices, fields, maps, polynomials, IPS) |
| Importable code | `python_la/` |
| Toolchain | **setuptools** via [`setup.py`](setup.py) (no `pyproject.toml` / uv yet) |
| Version | Hard-coded in `setup.py` (`VERSION`); also shown historically in older README titles — keep `setup.py` authoritative until a CD stamp lands |
| Tests | `tests/` (plus nested `*/tests` under the package); **never delete** |
| Secrets | Never commit `.pypirc`, API keys, tokens |

```text
.
├── python_la/           # Importable package
│   ├── la1/             # Fields, Vector, Matrix, Span, LinearMap, VectorSpace
│   ├── la2/             # Calculable/polynomials, BilinearForm, InnerProduct*
│   ├── utils/           # helpers + decorators
│   ├── other/           # Graph, Permutation
│   └── archive/         # Historical / unused — do not revive casually
├── tests/               # Primary pytest-style suite
├── setup.py             # Package metadata + install_requires
├── MANIFEST.in
├── README.md            # Marketing / user docs
├── LICENSE              # MIT
└── AGENTS.md
```

Default branch: **`main`**.

Shared CI/CD (when thin workflows are present): [`danielnachumdev/actions`](https://github.com/danielnachumdev/actions) (`@latest`, `standards-ref: latest`). How to adopt: [`HOW-TO-USE.md`](https://github.com/danielnachumdev/actions/blob/v1/HOW-TO-USE.md). Prefer required checks **`CI / CI`** and **`Semver / Semver`** once wired. Thin CI may use `allow-empty: true` until the suite is a reliable gate.

---

## Develop

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pip install pytest          # if not already available via danielutils workflows
pytest
# or: python -m pytest
```

| Task | Command |
| ---- | ------- |
| Import smoke | `python -c "import python_la; from python_la import Matrix, Vector"` |
| Tests | `pytest` from repo root (discover `tests/` and package-local tests) |

### Dependencies

- **Runtime:** `danielutils` (declared in `setup.py` `install_requires`)
- Prefer keeping the public surface re-exported through `python_la/__init__.py` → `la1` / `la2` / `utils` star imports unless deliberately narrowing the API.

---

## Code style & domain notes

- Follow the writing-python skill when adding/refactoring modules (class-first, SRP files, no stub shims).
- Keep math-facing APIs readable (method/property names that match course language: `kernel`, `characteristic_polynomial`, `to_orthonormal`, …).
- Nested READMEs under `python_la/la1/`, `la2/`, etc. are **implementation inventories** for humans browsing the tree — do not duplicate full CI/agent process there; keep that here.
- `python_la/archive/` is legacy; avoid new imports from it in production paths.
- Do **not** migrate to uv/`pyproject.toml` in a drive-by docs PR; treat packaging modernization as its own change with tests and install proof.

---

## PRs, CI, and releases

1. Branch off `main`; open a PR into `main`.
2. Attach **exactly one** semver label: `noBump` | `bumpPatch` | `bumpMinor` | `bumpMajor`.
3. When CI exists: thin orchestrators calling `danielnachumdev/actions`; Dependabot PRs stay on `noBump`.
4. Change shared CI/semver behavior in **`danielnachumdev/actions`**, not by re-vendoring here.
5. PyPI releases today are **manual** via the setuptools package (`python-la` on PyPI). Do not invent a local `publish.py` / quickpub path unless the repo explicitly adds one. Prefer Trusted Publishing / semver-cd later if CD is adopted.

### Sensitive / ignored

Do not commit: `.pypirc`, `.venv/`, `venv/`, `dist/`, `build/`, `*.egg-info/`, `__pycache__/`, API keys. Respect `.gitignore`.
