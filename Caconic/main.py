import sys
from sys import argv
try:
    argv[1]
except:
    sys.exit()
scriptpath = argv[1]
if not scriptpath.endswith(".co"):
    sys.exit()
import cmdparser
scriptlines = open(scriptpath).readlines()
print('\n'.join([' '.join([''.join(a) for a in cmdparser.handle_input(a)]) for a in scriptlines]))
