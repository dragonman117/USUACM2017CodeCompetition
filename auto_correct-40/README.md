# Auto correct

Your little sister is great as spelling, but not really good at typing. You often
cannot undestand the messages she sends you, so you decide to write a program to
help with her typing. Given a dictionary and a word not in the dictionary, this
program should determine if the word can be auto corrected, or give correction
suggestions.

The distance between any two words is the minimum number of characters that can be
inserted, deleted, or replaced in one word to obtain the other. A word can be auto
corrected if the shortest distance to a dictionary word is <= 2 and the shortest
distance word is unique.

## Input Format

The first line contains two integers `n` (number of words in the dictionary) and `k`
(number of words to check).

Each of the next `n` lines contains a dictionary word.

Each of the next `k` lines contains a word to check.

## Constraints
- 1 <= `n` <= 1000
- 1 <= `k` <= 100
- The length of each word is at leat 1 and at most 100

## Output Format

For each word to be checked, output "YES" followed by the auto-correct word if the
word is not in the dictionary and it can be auto corrected. Output "NO", followed by
any words with a distance <= 2 to the input word if the word is not in the dictionary
(if there are multiple such words, output them in lexicographical order). Output
"CORRECT" if the word is in the dictionary.


## Sample Input 1

```
4 3
apple
car
cat
dog
dog
can
aple
```

## Sample Output 1

```
CORRECT
NO car cat
YES apple
```

## Explanation 1

`dog` is in the dictionary, so it is a correct word.

`can` cannot be auto corrected because its distance to both `car` and `cat` is 1.

`aple` has a typo and can be auto corrected by adding a `p`.

------------------------
