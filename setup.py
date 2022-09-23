from setuptools import setup, find_packages
import codecs


def read_file(path: str) -> list[str]:
    with codecs.open(path, 'r', 'utf-8') as f:
        return [l.strip() for l in f.readlines()]


README_PATH = 'README.md'
VERSION = '0.96.5'
DESCRIPTION = 'Python linear algebra liabrary'
LONG_DESCRIPTION = '\n'.join(read_file(README_PATH))
setup(
    name="python-la",
    version=VERSION,
    author="danielnachumdev (Daniel Nachum)",
    author_email="<danielnachumdev@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "archive"]),
    install_requires=["danielutils"],
    keywords=['python', 'linear algebra', 'vector', 'matrix',
              'field', 'vector field', 'span', 'linear maps', 'bilinear form', 'inner product', 'linear transformation'],
    classifiers=[
        # "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
