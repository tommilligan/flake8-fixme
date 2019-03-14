import re

from .version import version

NOTE_REGEX = re.compile(r"(TODO|FIXME|XXX)")  # noqa


def check(physical_line):
    match = NOTE_REGEX.search(physical_line)
    if match:
        return match.start(), "FME000 Todo note found."


check.name = name = "flake8-fixme"
check.version = version
