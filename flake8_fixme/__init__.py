import re
from typing import Dict, Iterator, Match, NewType, Tuple

from .metadata import NAME, VERSION
from .utils import Code, code_from

Flake8Message = NewType("Flake8Message", str)
Flake8Result = NewType("Flake8Result", Tuple[int, Flake8Message])

WORD_CODES: Dict[str, Code] = {
    "FIXME": code_from("100"),  # noqa: T100
    "TODO": code_from("101"),  # noqa: T101
    "XXX": code_from("102"),  # noqa: T102
    "HACK": code_from("103"),  # noqa: T103
}

# Find any one of the note words definded above
RX_WORDS = re.compile("\\b({})\\b".format("|".join(WORD_CODES)))


def format_message(code: Code, word: str) -> Flake8Message:
    return Flake8Message("{} fixme found ({})".format(code, word))


def match_to_flake8_result(match: Match[str]) -> Flake8Result:
    word = match.group(1)
    code = WORD_CODES[word]
    result = Flake8Result((match.start(), format_message(code, word)))
    return result


def check(physical_line: str) -> Iterator[Flake8Result]:
    matches = RX_WORDS.finditer(physical_line)
    results = map(match_to_flake8_result, matches)
    yield from results


check.name = NAME  # type: ignore
check.version = VERSION  # type: ignore
