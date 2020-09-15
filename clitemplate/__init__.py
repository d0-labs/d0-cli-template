#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Invoke magic
from invoke import Collection, task

import clitemplate.tasks.module1.actions as module1_actions
import clitemplate.tasks.module2.actions as module2_actions

# Adding entire module to collection, and naming it "greetings"
ns = Collection(greetings=module1_actions)

# Adding a single task to the collection
ns.add_task(module2_actions.farewell)
