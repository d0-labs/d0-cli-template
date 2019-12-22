#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from ruamel.yaml import YAML


yaml = YAML()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Sets default environment to development unless env. is
if os.environ.get("D0_ENV") is None:
    os.environ["D0_ENV"] = "development"

with open(os.path.join(ROOT_DIR, "config.yml"), "r") as stream:
    try:
        configs = yaml.load(stream)
        APP_CONFIG = configs[os.environ.get("D0_ENV")]
    except Exception as error:
        print(error)

