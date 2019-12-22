#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from invoke import task
from clitemplate.definitions import APP_CONFIG


## ------------------


@task(
    help={"greeting": "Greeting to print"}
)
def test(c, greeting="Hello"):
    """
	This is a test action
	"""

    print(f"I'm a test action. Here's my greeting: [{greeting}]")


## ------------------
