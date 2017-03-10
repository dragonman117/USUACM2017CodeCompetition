#!/usr/bin/python
import sys

total = raw_input()
readin = raw_input()

data = dict()
kdata = dict()

for x in xrange(0, int(readin)):
    tmp = raw_input().split(" ")
    data[int(tmp[1])] = tmp[0]
    kdata[str(tmp[0])] = int(tmp[1])

readin = raw_input()

for x in xrange(0, int(readin)):
    tmp = raw_input()
    pval = int(total) - kdata[tmp]
    if pval in data.keys():
        sys.stdout.write(data[pval])
        if x < int(readin) - 1:
            sys.stdout.write("\n")
    else:
        sys.stdout.write("There is no matching snack Joe")
        if x < int(readin) - 1:
            sys.stdout.write("\n")