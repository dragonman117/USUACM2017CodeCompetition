# Poke Center Time Conversions

Oh No! Pikachu has fainted... I guess that last battle with rattata wasn't quite worth it. You
rush him to the nearest pokemon center, and while frantically pacing around the waiting room
you notice that all the clocks are in military time. You are smart enough to know how to read 
the clocks, however you notice schoolboy Alan keeps asking his teacher what the time is saying.

You decide to help, you walk over to the pc and decide to write a program that takes the military
time and converts it to be a 12-hour time notation (ex: 142316 is 02:23:16 PM). 

Please note: While most of the clocks in the Poke center are modern and go from 00:00:00 to 23:59:59, 
some of the older clocks will go from 01:00:00 to 24:59:59. As such your program must recognize
both 00:00:00 and 24:00:00 as 12:00:00 AM in the 12 hour notation.

------------------------

## Input format

1. The first line `n` is an integer for the number of times to read in and convert
2. Following lines will be a 6 digit integer of the format hhmmss

### Consraints
- 0 < `n` < 4294967296

### Sample Input
	10
	024353
	201234
	123201
	130222
	101159
	060606
	001453
	082837
	230645
	095821

### Sample Output
	02:43:53 AM
	08:12:34 PM
	12:32:01 AM
	01:02:22 PM
	10:11:59 AM
	06:06:06 AM
	12:14:53 AM
	08:28:37 AM
	11:06:45 PM
	09:58:21 AM

------------------------

- Note: This is a question that is solvible by CS 1 students