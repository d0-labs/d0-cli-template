from . import *

from invoke import Program
import toml, os

try:
    pyproject = toml.load(f"{os.getcwd()}/pyproject.toml", _dict=dict)
    version = pyproject["tool"]["poetry"]["version"]
except FileNotFoundError:
    version = None

program = Program(
    name="mycli",
    namespace=ns,
    version=version,
    binary="mycli",
    binary_names=["mycli"],
)
