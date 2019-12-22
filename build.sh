#! /bin/bash

package_name=$1
# version=$2
version=$(cat ${package_name}/_version.py | grep __version__ | cut -d '=' -f2 | tr -d "\"" | tr -d " ")

# Cleanup
rm -rf build
rm -rf dist
rm -rf ${package_name}.egg-info
find . -type d -name __pycache__ -exec rm -rf {} \;
pip uninstall -y ${package_name}

# Build package
python setup.py bdist_wheel

# Install package
pip install dist/${package_name}-${version}-py3-none-any.whl