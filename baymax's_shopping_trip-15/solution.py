#!/usr/bin/python

total = raw_input()

for i in xrange(0, int(total)):
    input = raw_input().split(" ")
    m = int(input[2])
    current = int(input[0])/int(input[1])
    free = current
    while free >= m:
        tmp = free/m
        current += tmp
        free = tmp
    print current