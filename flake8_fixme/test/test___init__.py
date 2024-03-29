from typing import List, Tuple

from flake8_fixme import check as _check

T100 = "T100 fixme found (FIXME)"
T101 = "T101 fixme found (TODO)"
T102 = "T102 fixme found (XXX)"
T103 = "T103 fixme found (HACK)"


def check(line: str) -> List[Tuple[int, str]]:
    """Check, but return a list not an iterator"""
    return list(_check(line))


def test_fixme() -> None:
    assert check("# FIXME") == [(2, T100)]
    assert check("# TODO in comment") == [(2, T101)]
    assert check("TODO this line") == [(0, T101)]
    assert check("# XXX") == [(2, T102)]
    assert check("# HACKY HACK HACK") == [(8, T103), (13, T103)]


def test_fixme_word_boundaries() -> None:
    assert check("# MASTODON") == []
    assert check("#TODO") == [(1, T101)]


def test_fixme_multiple() -> None:
    assert check("# TODO FIXME") == [(2, T101), (7, T100)]
