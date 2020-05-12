"""A CLI Box maker in Python.
This library can be used to create simple and beautiful
boxes in the terminal with ease.

:copyright: (c) 2020 Anish Jewalikar
:license: MIT, see LICENSE for more details.
"""

from .box import *
from .errors import TitlePositionError, TitleLengthError, DifferentLengthError
from .styles import RawStyle

__all__ = [
    "BoxFactory",
    "BoxStyles",
    "TitlePosition",
    "ContentAlignment",
    "TitlePositionError",
    "TitleLengthError",
    "DifferentLengthError",
    "RawStyle"
]

__title__ = "boxcli"
__author__ = "Anish Jewalikar"
__version__ = "1.3.0"
__license__ = "MIT"
