# Compensation

Bitman is working to save money for his summer trip abroad. So far he has been keeping
track of the time he has spent working on different days, but does not know how much
money he has earned. Help him figure out the total compensation for the time worked.

Time worked during weekends and time worked over 40 hours during weekdays in a single
week is paid at 150% of the hourly rate. The total compensation for all the time worked
is rounded to the nearest cent.

## Input Format

The first line contains an integer `w` (number of weeks) and a decimal `r` (hourly rate).

Each of the next `w` lines contains 7 integers representing the number of hours worked
during each day of a week, starting Monday.

## Output Format

Output the total compensation, including two decimal places for the cents.


## Constraints
- 1 < `w` < 10
- 1.00 < `r` < 100.00


## Sample Input 1

```
1 12.75
8 8 9 7 8 0 0
```

## Sample Output 1

```
510.00
```

## Explanation 1

The total number of hours is 40, so the total compensation is 12.75 * 40 = 510.00.


## Sample Input 2

```
1 12.75
8 8 9 7 8 1 0
```

## Sample Output 2

```
529.13
```

## Explanation 2

The total number of hours is 41, and one the hours is paid at 150% percent of the
hourly rate.


------------------------

- Note: This is a question that is solvable by CS 1 students
