# Snacking Problem

Joe has a problem. He has a backpack he is taking on competitive backpacking trip.
This trip has stringent rules as to how much his backpack can weigh, and Joe has 
only n  pounds for snacks. The rules for this competition also state that he is 
limited to exactly 2 snacks. 

Given a list of snacks, Joe is going to ask you to find what other snack he can take.
You know that each snack has a different weight, and if no snack is a compliment to
the snack that Joe asks about you will print "There is no matching snack Joe"

------------------------

## Input Format
1. Joes total weight limit
2. The number of snacks in Joe's list
3. The next lines will be the: snackName snackWeight
4. The first line after the snack list is the number of inquerys Joe will make
5. The following lines are the snackName of Joe's inquery

### Constraints

- Weigh limit < 110000
- Number of Snacks <= 100000
- Number of inquerys <= 50000

### Sample Input
	7
	5
	Banana-chips 3
	Trail-mix 6
	Carrots 4
	Snickers 5
	Apple 1
	3
	Carrots
	Snickers
	Trail-mix

### Sample Output
	Banana-chips
	There is no matching snack Joe
	Apple