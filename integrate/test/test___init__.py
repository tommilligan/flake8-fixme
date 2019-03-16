import subprocess


def test_flake8_output():
    result = subprocess.run(
        ["flake8", "--config", "integrate/setup.cfg", "integrate"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0

    assert result.stdout == (
        "integrate/__init__.py:2:7: T100 fixme found (FIXME)\n"
        "integrate/__init__.py:10:25: T101 fixme found (TODO)\n"
        "integrate/__init__.py:10:34: T102 fixme found (XXX)\n"
    )
