#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from invoke import task, exceptions
from clitemplate.definitions import APP_CONFIG

## ------------------

@task(
    help={"greeting": "Greeting to print"}
)
def test1(ctxt, greeting="Hello"):
    """
	Test action 1
	"""

    try:
        ctxt.config["action"] = "view"

        print(f"I'm test1 in the module1 module. Here's my greeting: [{greeting}]")

    except Exception as e:
        raise exceptions.Exit(
            f"ERROR! Cause: {str(e)}"
        )

## ------------------

@task(
    help={"greeting": "Greeting to print"},
)
def test2(ctxt, greeting="G'day"):
    """
	Test action 2
	"""

    print(f"I'm test2 in the module1 module. Here's my greeting: [{greeting}]")


## ------------------

@task(
    help={"greeting": "Greeting to print"},
    pre=[test1],
    post=[test2]
)
def test3(ctxt, greeting="Yo!"):
    """
	Test action 3
	"""
    try:

        print(f"I'm test3 in the module1 module. Here's my greeting: [{greeting}]")

    except Exception as e:
        raise exceptions.Exit(
            f"\n\nError. Cause: {str(e)}"
        )


