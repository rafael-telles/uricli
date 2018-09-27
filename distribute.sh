#!/usr/bin/env bash

python3 setup.py sdist
twine upload dist/uricli-*.tar.gz
rm -rf build dist;
