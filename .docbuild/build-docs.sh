#!/bin/bash

cd $(dirname $0)

make clean
rm -rf source/
rm -rf ../docs

sphinx-apidoc -o ./source ../phoebusgen

make html

cp -r _build/html/ ../docs
