#!/bin/bash

make clean
rm -rf source/

sphinx-apidoc -o ./source ../phoebusgen

make html

cp -r _build/html/ ../docs
