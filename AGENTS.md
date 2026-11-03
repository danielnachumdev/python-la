# python-la – Agent Context

Implementation guide for coding agents changing **python-la**. Product pitch and user-facing install: [`README.md`](README.md).

---

## Orientation

| Question | Answer |
| -------- | ------ |
| What is this? | Python **linear algebra** library (course-shaped API: matrices, fields, maps, polynomials, IPS) |
| Importable code | `python_la/` |
| Toolchain | [uv](https://docs.astral.sh/uv/) + `pyproject.toml` / `uv.lock` |
| Python | `>=3.11` (CI matrix **3.11, 3.12, 3.13**) |
| Version | Seeded at **0.97.0** to match current PyPI; CD stamps `pyproject.toml` from GitHub Release tags thereafter |
| Tests | `tests/` — pytest; **never delete** |
| Secrets | Never commit `.pypirc`, API keys, tokens |

```text
.
├── .github/             # CODEOWNERS, dependabot.yml, thin CI/CD orchestrators
├── python_la/           # Importable package
│   ├── la1/             # Fields, Vector, Matrix, Span, LinearMap, VectorSpace
│   ├── la2/             # Calculable/polynomials, BilinearForm, InnerProduct*
│   ├── utils/           # helpers + decorators
│   ├── other/           # Graph, Permutation
│   └── archive/         # Historical / unused — do not revive casually
├── tests/               # Primary pytest suite
├── pyproject.toml
├── uv.lock
├── README.md            # Marketing / user docs
├── LICENSE              # MIT
└── AGENTS.md
```

Default branch: **`main`**.

Shared CI/CD: [`danielnachumdev/actions`](https://github.com/danielnachumdev/actions) (this repo pins **`@latest`**). How to adopt: [`HOW-TO-USE.md`](https://github.com/danielnachumdev/actions/blob/v1/HOW-TO-USE.md). Prefer required checks **`CI / CI`** and **`Semver / Semver`**.

---

## Develop

```bash
uv sync                 # runtime only → .venv
uv sync --group dev     # + pytest, …
# or: uv sync --all-groups
```

`tool.uv.default-groups` is empty — `uv sync` does **not** install `dev` by default. CI uses `uv sync --group dev`.

| Task | Command |
| ---- | ------- |
| Import smoke | `uv run python -c "import python_la; from python_la import Matrix, Vector"` |
| Tests | `uv run pytest` |

### Dependencies

- **Runtime:** `danielutils==0.7.0` — verified with this suite; still exports multi-arg `@validate`, `NotImplemented`, `abstractmethod`, and `TestFactory` / `Test`. Do not bump without re-running the full suite and (for ≥0.7.8) fixing Windows/`screeninfo` import, or (for ≥0.8) migrating off the old validate / TestFactory APIs.
- **Dev group:** pytest, pytest-cov, pytest-xdist, setuptools
- Prefer editing deps in `pyproject.toml` and regenerating with `uv lock` / `uv sync --group dev`

---

## Code style & domain notes

- Follow the writing-python skill when adding/refactoring modules (class-first, SRP files, no stub shims).
- Keep math-facing APIs readable (method/property names that match course language: `kernel`, `characteristic_polynomial`, `to_orthonormal`, …).
- Nested READMEs under `python_la/la1/`, `la2/`, etc. are **implementation inventories** for humans browsing the tree — do not duplicate full CI/agent process there; keep that here.
- `python_la/archive/` is legacy; avoid new imports from it in production paths.
- Public surface is re-exported through `python_la/__init__.py` → `la1` / `la2` / `utils` star imports unless deliberately narrowing the API. `__version__` is `importlib.metadata.version("python-la")` (fallback `"0.0.0"` if not installed).

---

## PRs, CI, and releases

1. Branch off `main`; open a PR into `main`.
2. Attach **exactly one** semver label: `noBump` | `bumpPatch` | `bumpMinor` | `bumpMajor`.
3. **CI** — `…/ci.yml@latest` (tests) + `…/semver-ci.yml@latest` (validate label). Prefer **`CI / CI`** and **`Semver / Semver`**.
4. **CD** — `…/semver-cd.yml@latest` after CI succeeds on `main`: bump → wheel → GitHub Release → floating `vMAJOR` → **PyPI** (`publish-pypi: true`), or skip on `noBump`.
5. Version **source of truth** is GitHub Release tags. If none yet, CD seeds from `pyproject.toml` (**0.97.0** = current PyPI).
6. Dependabot PRs stay on `noBump` (auto-merge workflow present).
7. Change shared CI/semver behavior in **`danielnachumdev/actions`**, not by re-vendoring here.

**PyPI:** shipped only via CD (Trusted Publishing OIDC preferred for repo + workflow `cd.yml`; optional repo secret `PYPI_API_TOKEN`). Thin CD must grant `id-token: write` and pass `PYPI_API_TOKEN` by name. There is no local `publish.py` / quickpub path.

### Repo gates (already configured)

- `.github/CODEOWNERS` — `@danielnachumdev`
- Branch protection / ruleset: required **`CI / CI`** + **`Semver / Semver`**; code-owner reviews; no force-push to `main`
- Private vulnerability reporting via GitHub Security Advisories

---

## Sensitive / ignored

Do not commit: `.pypirc`, `.venv/`, `venv/`, `dist/`, `__pycache__/`, API keys, coverage HTML (`htmlcov/`). Track `uv.lock`. Respect `.gitignore`.
