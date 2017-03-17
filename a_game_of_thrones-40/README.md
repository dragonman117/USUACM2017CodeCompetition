# A Game of Thrones

"When you play the game of thrones you win or you die" - George R.R. Martin

You have started reading the Game of Thrones book series, yay! However, you ran into a little problem
you are having trouble keeping track of who belongs to which faction as well as which factions 
are all battling for the throne. (Note: a faction is being defined as a leiege lord and who follows them, and a liege lord follows no one)

You decide to write a program to help keep track of what is going on. You begin by entering all the 
different characters names, you then enter each character name followed by who they follow/serve.
Once you enter all the data it then reports how many different factions are fighting for the thone by saying 
"There are x factions playing the game of thrones", and you can then ask who each person belongs to. 


------------------------

## Input Format
1. The first line is the number of charachters `c` you will enter
2. The following lines are the names of the characters (one per line)
3. The next line is the number of alligences `a` you will enter
4. The following lines will be the name of the character followed by a comma, and the name of their alleginece
5. The next line is the number of inqueries `i` that will be asked
6. Following lines will be the name of the inquery made

### Constraints
- 5 < `c` < 100000
- 1 < `a` < `c`
- 1 < `i` < `c`

### Sample Input
	9
	Tyrion Lannister
	Jaime Lannister
	Cersei Lannister
	Daenerys Targaryen
	Jon Snow
	Sansa Stark
	Brienne of Tarth
	Roose Bolton
	Tywin Lannister	
	6
	Tyrion Lannister, Daenerys Targaryen
	Jaime Lannister, Cersei Lannister
	Jon Snow, Sansa Stark
	Brienne of Tarth, Sansa Stark
	Roose Bolton, Tywin Lannister
	Cersei Lannister, Tywin Lannister
	4
	Tyrion Lannister
	Jon Snow
	Sansa Stark
	Jaime Lannister

### Sample Ouptut
	There are 3 factions playing the game of thrones
	Daenerys Targaryen
	Sansa Stark
	Sansa Stark
	Tywin Lannister
