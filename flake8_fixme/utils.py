import re
from typing import NewType

from .metadata import CODE_STEM

Code = NewType("Code", str)

RX_CODE_LEAF_VALID = re.compile(r"[1-9]\d+")


def code_from(code: str) -> Code:
    """Create an error code for this plugin from the given number"""
    # Check the numerical part of the error code is valid
    assert RX_CODE_LEAF_VALID.match(code)

    return Code("".join((CODE_STEM, code)))
