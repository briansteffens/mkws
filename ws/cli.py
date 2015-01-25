#!/usr/bin/env python3

"""
usage:
    ws init <template> [options]
    ws open [options]

    -h, --help  show help screen

"""

import os
import sys
from subprocess import call

from docopt import docopt
args = docopt(__doc__)

templates = os.path.split(os.path.realpath(__file__))[0]+"/templates/"

if args["init"]:
    template = templates+args["<template>"]

    if os.path.exists(".ws"):
        print("A workstation already exists here (path: ./.ws)")
        sys.exit(1)

    if not os.path.exists(template):
        print("No template found at ["+template+"]")
        sys.exit(1)

    call(["cp -r "+template+"/* ./"],shell=True)
    call(["cp -r "+template+"/.ws ./"],shell=True)

if args["open"] or args["init"]:
    call(["./.ws/open"])

else:
    raise NotImplemented("Unable to parse command")
