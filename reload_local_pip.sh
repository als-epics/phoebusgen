#!/bin/bash

echo y | pip uninstall phoebusgen
rm -rf build
python3 setup.py sdist bdist_wheel
pip install --user . 

