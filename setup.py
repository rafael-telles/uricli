# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('uricli/uricli.py').read(),
    re.M
).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="uricli",
    packages=["uricli"],
    entry_points={
        "console_scripts": ['uri = uricli.uricli:main']
    },
    version=version,
    description="Utility CLI for submitting solutions to URI Online Judge.",
    long_description=long_descr,
    author="Rafael Telles",
    author_email="rafael@telles.pw",
    install_requires=[
        "docopt==0.6.2",
        "PyInquirer==1.0.2",
        "requests==2.19.1",
        "mechanicalSoup==0.11.0",
        "demjson==2.2.4",
    ],
    url="https://github.com/rafael-telles/uri-cli",
)
