from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.95'
DESCRIPTION = 'Python linear algebra liabrary'

# Setting up
setup(
    name="python-la",
    version=VERSION,
    author="danielnachumdev (Daniel Nachum)",
    author_email="<danielnachumdev@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
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
