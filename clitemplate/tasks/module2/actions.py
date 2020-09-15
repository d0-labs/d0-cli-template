#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from invoke import task
from clitemplate.definitions import APP_CONFIG


## ------------------


@task(
    help={"goodbye": "Parting words to print"}
)
def farewell(ctxt, goodbye="Later, skater!"):
    """
	This is a test action
	"""

    print(f"I'm test in the module2 module. Here are my parting words: [{goodbye}]")


## ------------------
