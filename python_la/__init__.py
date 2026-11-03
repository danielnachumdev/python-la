from importlib.metadata import PackageNotFoundError, version

from .la1 import *
from .la2 import *
from .utils import *

try:
    __version__ = version("python-la")
except PackageNotFoundError:  # pragma: no cover - editable / source tree
    __version__ = "0.0.0"
