from flake8_fixme import check as _check

T100 = "T100 Fixme found (FIXME)"
T101 = "T101 Fixme found (TODO)"
T102 = "T102 Fixme found (XXX)"


def check(line):
    """Check, but return a list not an iterator"""
    return list(_check(line))


def test_fixme():
    assert check("# FIXME") == [(2, T100)]
    assert check("# TODO in comment") == [(2, T101)]
    assert check("TODO this line") == [(0, T101)]
    assert check("# XXX") == [(2, T102)]


def test_fixme_word_boundaries():
    assert check("# MASTODON") == []
    assert check("#TODO") == [(1, T101)]


def test_fixme_multiple():
    assert check("# TODO FIXME") == [(2, T101), (7, T100)]
