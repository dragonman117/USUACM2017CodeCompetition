#Baymax's Shopping Trip

Baymax has a problem, it is Hiro's birthday and he would like to get him his favorite candy bar.
The local store is having a sale, where for every `n` candybars that Baymax buys he gets one free.
This sale is especially good in that each free candybar he gets counts as another candybar purchased.

For example Baymax has 10 dollars, the candybar cost 2 dollars each, and the sale is buy 2 get 
one free. In this senario Baymax initially gets 5 candybars, then because he bought more than 4 candybars
he gets 2 more for free. These 2 free ones in turn count as another 2 purchased giving him another 1 bar. 
This means that in this seario Baymax can get a total of 8 total bars.

Can you help Baymax find out how many candybars he can get in different senarios?

------------------------

## Input Format
1. `t` is the number of senarios Baymax wishes to run
2. `n` is the money Baymax has (in whole numbers)
3. `c` is the cost of the candybars (whole number)
4. `m` is the number of bars to purchase to get one free

###
	`t`
	`n` `c` `m`

###Constraints
- 1 < `t` < 1000
- 2 < `n` < 10^5
- 1 < `c` < n
- 2 < `m` < n

###Sample Input
	3
	10 2 2
	9 2 3
	20 3 5

###Sample Output
	8
	5
	7

------------------------

- Note: This is a question that is solvible by CS 1 students
