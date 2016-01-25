#!/usr/bin/env python
import sys

prev_show = "  "
running_total = 0
abc_found = False

for line in sys.stdin:
    line = line.strip()
    key_value  = line.split('\t')

    curr_show = key_value[0]
    value_in = key_value[1]

    if value_in[0:3]=='ABC':
        abc_found = True
    elif curr_show != prev_show:
        if abc_found:
            print("{0}\t{1}".format(prev_show, running_total))
        running_total = int(value_in)
        prev_show = curr_show
        abc_found = False
    else:
        running_total += int(value_in)
