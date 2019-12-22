#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from ._version import (
    __version__,
)  # Need the "." before "_version" because invoke also has a "_version.py"

# Invoke magic
from invoke import Collection, task

from .tasks.libname import actions

# See docs: http://docs.pyinvoke.org/en/1.3/concepts/namespaces.html
ns = Collection.from_module(actions)
