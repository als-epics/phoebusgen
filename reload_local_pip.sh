#!/bin/bash

echo y | pip3 uninstall phoebusgen
rm -rf build
python3 setup.py sdist bdist_wheel
pip3 install --user .
