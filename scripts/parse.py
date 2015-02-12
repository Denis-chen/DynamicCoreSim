#!/usr/bin/env python
# parse.py
# Read in a gem5 stats file and parse it into CSV file

import os

def parse_line(arr):
    result = []
    index = 0
    for index, item in enumerate(arr):
        if item == '#':
            index = index + 1
            break
    result = arr[0:3]
    desc = ''
    for i in range(index, len(arr)):
        desc = desc + arr[i] + ' ' 
    result[2] = desc
    return result

def parse_stats():
    stats = {}
    next_id = -1

    f = open("stats.txt")
    for line in f:
        if line == '---------- Begin Simulation Statistics ----------\n':
            next_id = next_id + 1
            stats[next_id] = []
        elif line == '---------- End Simulation Statistics   ----------\n':
            pass
        else:
            l = line.split()
            if len(l) >= 3:
                l = parse_line(l)
                s = {}
                s['field'] = l[0]
                s['value'] = l[1]
                s['description'] = l[2]
                stats[next_id].append(s)

    out = 'FIELD;BOOT;JPEG;OCEAN;EPIC;FFT;GSM;LU;ADPCM;RADIX;SHUTDOWN;DESCRIPTION\n'

    for row in stats[0]:
        out = out + row['field'] + ';'
        for sim_id, sim in stats.iteritems():
            for sim_row in sim:
                field_found = False
                if sim_row['field'] == row['field']:
                    out = out + sim_row['value'] + ';'
                    field_found = True
                    break
            if not field_found:
                out = out + ';'
        out = out + row['description'] + '\n'
    return out

for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        os.chdir(subdirname)
        filename = '../' + subdirname + '.csv'
        with open(filename, "w") as out:
            out.write(parse_stats())
        print "Wrote csv file '%s.csv'." % subdirname
        os.chdir('..')
