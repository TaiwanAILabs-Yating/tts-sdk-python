#!/bin/bash

echo "Start to build package"
python setup.py sdist bdist_wheel

echo "Upload package to testing PyPI"
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

echo "Clean up build package"
rm -rf Yating_TTS_SDK.egg-info/ build/ dist/
