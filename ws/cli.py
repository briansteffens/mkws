#!/usr/bin/env python3

"""
usage:
    ws init <template> [options]
    ws open [options]

    -h, --help  show help screen

"""

import os
import sys
import random
from subprocess import call

from docopt import docopt
args = docopt(__doc__)

# Make a random ID, 10 chars long, using 0-9, A-Z, a-z, -, and _ as digits
def generate_ws_id():
    ret = ''

    for i in range(10):
        c = random.randrange(0, 65)

        # 0-9
        if c < 10:
            ret += str(c)
            continue

        c -= 10

        # A-Z
        if c < 26:
            ret += chr(c + 65)
            continue

        c -= 26

        # a-z
        if c < 26:
            ret += chr(c + 97)
            continue

        # - and _
        if c == 0:
            ret += "-"
        else:
            ret += "_"

    return ret

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

    with open('.ws/id', 'w') as f:
        f.write(generate_ws_id())


if args["open"] or args["init"]:
    with open('.ws/id', 'r') as f:
        os.environ['WS_SESSION'] = 'ws-' + f.read()

    call(["./.ws/open"])

else:
    raise NotImplemented("Unable to parse command")
