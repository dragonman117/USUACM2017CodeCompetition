#!/usr/bin/python

def buff(x):
    tmp = "0" + str(x)
    return tmp[-2:]

count = int(raw_input())

for x in xrange(0, count):
    tmp = raw_input()
    hr = int(tmp[0:2])
    min= tmp[2:4]
    sec= tmp[4:6]
    if hr > 12 and hr != 24:
        print(buff(hr-12) + ":" + min + ":" + sec + " PM")
    elif hr == 00 or hr == 24:
        print("12" + ":" + min + ":" + sec + " AM")
    else:
        print(buff(hr) + ":" + min + ":" + sec + " AM")