import re
import fileinput

for line in fileinput.input():
    print "{:>6}  {}".format(fileinput.lineno(), line),

