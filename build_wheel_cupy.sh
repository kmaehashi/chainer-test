#!/bin/sh -ex

cd cupy
pip install wheel
python setup.py -q bdist_wheel
