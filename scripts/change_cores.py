#!/usr/bin/env python
import sys

LINE = 3

f = open(r'/home/david/Desktop/comp_arch_sims/gem5-stable/configs/boot/dynamic_processor.rcS', 'r')    # pass an appropriate path of the required file
lines = f.readlines()
lines[LINE-1] = "CORES=%s\n" % sys.argv[1]    # n is the line number you want to edit; subtract 1 as indexing of list starts from 0
f.close()   # close the file and reopen in write mode to enable writing to file; you can also open in append mode and use "seek", but you will have some unwanted old data if the new data is shorter in length.

f = open(r'/home/david/Desktop/comp_arch_sims/gem5-stable/configs/boot/dynamic_processor.rcS', 'w')
f.writelines(lines)
f.close()