# Movie Golf
Ross and Laurel have created a game caled movie golf. The game consists of a player (the challenger) selecting two movies. The other player (the defender) must then find and return the distance between two movies. The distance between two movies is the number of movies linked by actors between each movie.

For example if two players were playing, and the challenger gave the movies "Jurassic World" and "Passengers" then the Golf Score would be 1 ("Jurassic World" stars Chris Pratt, who also stars in "Passengers"). However if the challenger gave the movies "Passengers" and "Logan" the movie score would be 2 ("Passengers" stars Jennifer Lawrence, who stars in "X-Men: Days of Future Past" that stars "Hugh Jackman", who stars in "Logan"). If no connection is found between two movies, then the player informs the challenger that there is "No Connection".

You are writting a program to help Ross and Laurel judge if they have found the best connection. You will be given a list of actors in the movies, a list of movies, and a list of which actor is in which movie. You will then be given a list of the challenges given, you will then report the movie golf number (minimum number) or if there is no link between two movies you will report "No Connection"

### A note on how the inputs are constructed

All input was gleaned from IMDB's website (http://www.imdb.com/) any intelectual property belogns to them. Due to limitations with hacker rank, each test case contians a limited number of movies, and does not contain full cast lists, only the top actors listed on the movies initial page. The input was built by pulling all actors/movie assosications, then actors was build by copying this list and deleteing movie info, finally movies was created by listing unique movies. This information was provided in order to help you understand how test cases were constructed to allow you to test your own solutions prior to submission.

------------------------

## Input Format
1. The first line is 4 numbers `n`, `m`, `o`, `p`
2. `n` is the number of actors directly following. Each actor is encapsulated in "", this set may contain duplicates
3. `m` is the number of movies. Each movie title is encapsulated in "".
4. `o` is the number of connections "actor","movies" following the actor/movie lists
5. `p` is the number of challenges "movie a","movie b" that will be asked

### Constraints

### Sample Input
	45 3 45 2
	"Jennifer Lawrence"
	"Chris Pratt"
	"Michael Sheen"
	"Laurence Fishburne"
	"Andy Garcia"
	"Vince Foster"
	"Kara Flowers"
	"Conor Brophy"
	"Julee Cerda"
	"Aurora Perrineau"
	"Lauren Farmer"
	"Emerald Mayne"
	"Kristin Brock"
	"Tom Ferrari"
	"Quansae Rutledge"
	"Hugh Jackman"
	"James McAvoy"
	"Michael Fassbender"
	"Jennifer Lawrence"
	"Halle Berry"
	"Nicholas Hoult"
	"Anna Paquin"
	"Ellen Page"
	"Peter Dinklage"
	"Shawn Ashmore"
	"Omar Sy"
	"Evan Peters"
	"Josh Helman"
	"Daniel Cudmore"
	"Bingbing Fan"
	"Hugh Jackman"
	"Patrick Stewart"
	"Dafne Keen"
	"Boyd Holbrook"
	"Stephen Merchant"
	"Elizabeth Rodriguez"
	"Richard E. Grant"
	"Eriq La Salle"
	"Elise Neal"
	"Quincy Fouse"
	"Al Coronel"
	"Frank Gallegos"
	"Anthony Escobar"
	"Reynaldo Gallegos"
	"Krzysztof Soszynski"
	"Passengers"
	"X-Men: Days of Future Past"
	"Logan"
	"Jennifer Lawrence","Passengers"
	"Chris Pratt","Passengers"
	"Michael Sheen","Passengers"
	"Laurence Fishburne","Passengers"
	"Andy Garcia","Passengers"
	"Vince Foster","Passengers"
	"Kara Flowers","Passengers"
	"Conor Brophy","Passengers"
	"Julee Cerda","Passengers"
	"Aurora Perrineau","Passengers"
	"Lauren Farmer","Passengers"
	"Emerald Mayne","Passengers"
	"Kristin Brock","Passengers"
	"Tom Ferrari","Passengers"
	"Quansae Rutledge","Passengers"
	"Hugh Jackman","X-Men: Days of Future Past"
	"James McAvoy","X-Men: Days of Future Past"
	"Michael Fassbender","X-Men: Days of Future Past"
	"Jennifer Lawrence","X-Men: Days of Future Past"
	"Halle Berry","X-Men: Days of Future Past"
	"Nicholas Hoult","X-Men: Days of Future Past"
	"Anna Paquin","X-Men: Days of Future Past"
	"Ellen Page","X-Men: Days of Future Past"
	"Peter Dinklage","X-Men: Days of Future Past"
	"Shawn Ashmore","X-Men: Days of Future Past"
	"Omar Sy","X-Men: Days of Future Past"
	"Evan Peters","X-Men: Days of Future Past"
	"Josh Helman","X-Men: Days of Future Past"
	"Daniel Cudmore","X-Men: Days of Future Past"
	"Bingbing Fan","X-Men: Days of Future Past"
	"Hugh Jackman","Logan"
	"Patrick Stewart","Logan"
	"Dafne Keen","Logan"
	"Boyd Holbrook","Logan"
	"Stephen Merchant","Logan"
	"Elizabeth Rodriguez","Logan"
	"Richard E. Grant","Logan"
	"Eriq La Salle","Logan"
	"Elise Neal","Logan"
	"Quincy Fouse","Logan"
	"Al Coronel","Logan"
	"Frank Gallegos","Logan"
	"Anthony Escobar","Logan"
	"Reynaldo Gallegos","Logan"
	"Krzysztof Soszynski","Logan"
	"Passengers","Logan"
	"Passengers","X-Men: Days of Future Past"

## Sample Output
	2
	1