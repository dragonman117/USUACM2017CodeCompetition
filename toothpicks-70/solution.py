def close_enough(observed, expected, tolerance):
    return abs(observed - expected) <= tolerance

def fixed_point_iteration(funct, x, tolerance):
    guess0 = x
    guess = funct(guess0)

    while not close_enough(guess0, guess, tolerance):
        guess0 = guess
        guess = funct(guess0)

    return guess

def solve_triangle(y):
    x = int(fixed_point_iteration(lambda x: (2*y/(x+1) + x) / 2, 1, .0001)) + 1

    if x * (x + 1) // 2 > y:
        x -= 1

    return x

def solve_sum_of_squares(y):
    x = int(fixed_point_iteration(lambda x: (6*y/(x+1)/(2*x+1) + x) / 2, 1, .0001)) + 1

    if x * (x + 1) * (2*x + 1) // 6 > y:
        x -= 1

    return x

def triangle(n):
    return n * (n + 1) // 2

def sum_of_squares(n):
    return n * (n + 1) * (2*n + 1) // 6

# SOLUTION
def answer(s):
    if s == 1:
        return 4

    n = solve_sum_of_squares(s)

    s -= sum_of_squares(n)
    toothpicks = 2*n*(n+1)
    if s == 0:
        return toothpicks

    if s - 1 < triangle(n):
        s -= 1
        toothpicks += 3

        i = solve_triangle(s)

        toothpicks += i * 2

    else:
        s -= 2
        toothpicks += 6
        s -= triangle(n) - 1
        toothpicks += 2 * (n - 1)

        i = solve_triangle(s)

        toothpicks += i * 2

    return toothpicks

# MAIN
if __name__ == "__main__":
    for _ in range(int(input())):
        print(answer(int(input())))
