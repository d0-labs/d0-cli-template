from setuptools import find_packages, setup

_locals = {}
with open("clitemplate/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(
    name="clitemplate",
    version=version,
    url="https://github.com/d0-labs/d0-cli-template",
    author="Adriana Villela, Bernard Otu",
    author_email="adriana@dzerolabs.io, bernard@dzerolabs.io",
    install_requires=["invoke"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={"console_scripts": ["mycliname = clitemplate.main:program.run"]},
)
