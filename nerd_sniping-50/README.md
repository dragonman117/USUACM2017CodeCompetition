# Nerd Sniping

"There's a certain type of brain that's easily disabled. If you show it an interesting problem, it involuntarily drops everything else to work on it." - Randall Munroe

Finding prime numbers is an activity that nerds love, with the excuse that they're "useful in cryptography or something." A prime number is any integer greater than 1 that is divisible by only 1 and itself - 2, 3, 5, and 7 are the first four prime numbers.

Let's define a (made-up) word: "primacity." The primacity of a number is the number of divisors it has that are prime numbers, excluding 1 but including itself. The primacities of some example numbers are given below:

    1 - 0   // By definition - 1 is not prime, and its only divisor
    2 - 1   // 2 is divisible only by 1 and 2 (making it prime), and of those 2 is a prime, so its primacity is 2.
    3 - 1   // All prime numbers have a primacity of 1, by the same logic as (2)
    4 - 1   // 4 is divisible by 1, 2, and 4, and of those three only 2 is prime.
    6 - 2   // 6 is divisible by primes 2 and 3 (1 and 6 are not prime)
    12 - 2  // 12 is divisible by 2, 3, 4, 5, and 6, but of those only 2 and 3 are primes

Just asking the primacity of a single number is entirely too boring, so instead I'm going to give you a range of numbers `[A, B]` to search, and a primacity value `K`. I want you to tell me how many integers between A and B (inclusive) have a primacity of exactly `K`.

Consider yourself nerd sniped!

## Input format

1. The first line `T` is the number of problems that you need to solve in this problem.
2. The next `T` lines will contain three numbers, each separated by a space - `A`, `B`, and `K`, respectively.

## Expected output

1. Each line will contain a single number `N`, the number of integers with primacity `K` between `A` and `B` (including `A` and `B`)

### Constraints

- 1 ≤ `T` ≤ 100
- 2 ≤ A ≤ B ≤ 10^7
- 1 ≤ K ≤ 10^9

### Sample Input

```
5
5 15 2
2 10 1
24 42 3
1000000 1000000 1
1000000 1000000 2
```

### Sample Output

```
5
7
2
0
1
```

------------------------

- Note: This problem is derived from https://www.facebook.com/hackercup/problem/582396081891255/, and attribution must be given as per https://creativecommons.org/licenses/by-nc/3.0/. It probably shouldn't be given in the problem itself (lest people look up the solution), but it should be mentioned that this problem came from there, and after-the-fact versions should retain the attribution.