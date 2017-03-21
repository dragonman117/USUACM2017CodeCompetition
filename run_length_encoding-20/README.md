# Run Length Encoding

Rachael is trying to send a message to her friends Lisa, and Emma. Unfortunately
her network connection is slow right now and she wants her friends to receive the
message as quickly as possible.

She remembers hearing Lisa and Emma talking about run length encoding. If she can
use it to make the message shorter, then it can be transmitted faster. Help her
write a program that compresses the message using run length encoding.

In a run length encoded string, character runs are compressed by storing the
length of the run and the character. For example, the string "AAABBBBBCCCCCCC"
is encoded as "3A5B7C" and the string "Emma" is encoded as "1E2m1a".


## Input Format

There is a single line of input with the message.

## Constraints
- The message only contains alphabetic characters
- The message length it at least 1 and most 10000


## Output Format

Output "YES" followed by a space and the run length encoded message, if the encoded
message is shorter than the original message.

Output "NO" if the encoded message is not shorter than the original message.


## Sample Input 1

```
RunLisaRun
```

## Sample Output 1

```
NO
```

## Explanation 1

The encoded message is `1R1u1n1L1i1s1a1R1u1n`, which is longer than the input message.


## Sample Input 2

```
AAABBBBBCCCCCCC
```

## Sample Output 2

```
YES 3A5B7C
```

## Explanation 2

The encoded message is `3A5B7C`, which is shorter than the input message.



------------------------

- Note: This is a question that is solvable by CS 2 students
