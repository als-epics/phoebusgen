#!/bin/bash

rm -rf build
rm -rf phoebusgen.egg-info
rm -rf dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/* --verbose
