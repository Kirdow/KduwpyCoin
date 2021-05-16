#!/bin/sh

echo =================================
echo == INSTALLING REQUIRED MODULES ==
echo =================================

pip3 install pycryptodome
pip3 install pybase62

echo ================
echo == KduwpyCoin ==
echo ================

python3 Main.py

echo ===========
echo == ENDED ==
echo ===========


