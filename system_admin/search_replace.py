#!/usr/bin/env python
"""
https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s04.html
"""

import os # os module offers low level Linux/Windows system calls
import sys

# Argument List len assigned to nargs
nargs = len(sys.argv)

if not 3 <= nargs <= 5:
    print("usage: %s search_text replace_text [infile [outfile]]" % \
        os.path.basename(sys.argv[0]))
    ## Execute from cli
    # search_replace.py xvu bbb passwd_copy1.txt passwd_copy2.txt
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input = sys.stdin
    output = sys.stdout
    if nargs > 3:
        input = open(sys.argv[3])
    if nargs > 4:
        output = open(sys.argv[4], 'w')
    for s in input.readlines(  ):
    #for s in input.xreadlines(  ):
        substitute_txt = '{:80}'.format(rtext) # added by me
        output.write(s.replace(stext, substitute_txt))
    output.close(  )
    input.close(  )