#!/usr/bin/env python
import sys

for line in sys.stdin:

    line = line.strip()
    key_value  = line.split(",")
    key_in     = key_value[0].split(" ")
    value_in   = key_value[1]

    if value_in[0:3]=='ABC':
        print( '%s\t%s' % (key_in[0], value_in) )
    elif value_in.isdigit():
        print( '%s\t%s' % (key_in[0], value_in) )
