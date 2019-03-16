# coding: utf-8

from __future__ import with_statement

from setuptools import setup

from flake8_fixme.metadata import CODE_STEM, NAME, VERSION


def get_readme() -> str:
    with open("README.md") as readme_handle:
        return readme_handle.read()


setup(
    name=NAME,
    version=VERSION,
    description="FIXME and TODO checker. Plugin for flake8.",  # noqa: T
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    keywords="flake8 plugin fixme todo xxx hack",
    author="Tom Milligan",
    author_email="tommilligan@users.noreply.github.com",
    url="https://github.com/tommilligan/flake8-fixme",
    license="Apache-2.0",
    packages=["flake8_fixme"],
    install_requires=[],
    zip_safe=False,
    entry_points={"flake8.extension": ["{} = flake8_fixme:check".format(CODE_STEM)]},
    classifiers=[
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
