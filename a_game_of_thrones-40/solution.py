#!/usr/bin/python

def trace(list, start):
    while list[start] != -1:
        start = list[start]
    return start

ref = dict()
rlookup = dict()
data = []

tmpCount = int(raw_input())
for i in xrange(0, tmpCount):
    line = raw_input()
    ref[line] = i
    rlookup[i] = line
    data.append(-1)

tmpCount = int(raw_input())
for i in xrange(0, tmpCount):
    line = [x.strip() for x in raw_input().split(",")]
    data[ref[line[0]]] = ref[line[1]]

factions = 0
for char in data:
    if char == -1:
        factions += 1

print "There are " + str(factions) + " factions playing the game of thrones"

tmpCount = int(raw_input())
for i in xrange(0, tmpCount):
    line = raw_input()
    print rlookup[trace(data, ref[line])]
