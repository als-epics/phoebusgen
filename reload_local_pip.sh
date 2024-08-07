#!/bin/bash

echo y | pip3 uninstall phoebusgen
rm -rf build
rm -rf phoebusgen.egg-info
rm -rf dist
python3 -m build
pip3 install --user .
