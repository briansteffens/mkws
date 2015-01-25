import os
from subprocess import call

wsroot = os.path.split(os.path.realpath(__file__))[0]

call(["ln","-s",wsroot+"/ws/cli.py","/usr/bin/ws"])
