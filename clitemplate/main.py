from . import *

from invoke import Program

from ._version import __version__


version = __version__

program = Program(
    name="mycliname",
    namespace=ns,
    version=version,
    binary="mycliname",
    binary_names=["mycliname"],
)
