# Problems for Spring 2017 ACM Code Competition

We're planning on having 20 questions total, so write a lot of them!

Each problem should have:

- a description
- an estimated difficulty level
- 4-6 test cases
- a solution in at least two languages (C++, Python, or whatever)

Put each problem in it's own directory named with following conventions:

    snake_case_name-<difficulty level in minutes>

For example, `best_words-20` is a problem named "Best Words" that has a
difficulty of 20 minutes.

--------------

### Running test cases

To run a test case on a solution, pipe the test case to the solution's
executable:

C++

    cat testCase0.txt | ./solution

Python

    cat testCase0.txt | python solution.py

----------------

### Difficulty Scale

With teams of 3 and 4 hours to code, only 36 minuetes can be spent on each
problem to solve all 20 of them.

Gauge the difficulty of problems in the estimated number of minutes that
it would take one person to solve the question. For example:

> If a problem takes 25 minutes, it has a difficulty of 25

_NOTE: We need to make sure we don't overestimate or underestimate difficulty_

