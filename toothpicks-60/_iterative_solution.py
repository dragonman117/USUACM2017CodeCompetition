from numpy import roots
import itertools

def triangle(n):
  return n * (n + 1) // 2

def sum_of_squares(n):
  return n * (n + 1) * (2*n + 1) // 6

def polynomial(coef, x):
  y = 0

  for i, c in enumerate(reversed(coef)):
    y += c * x**i

  return y

def solve(coefs):
  n = int(roots(coefs).real[-1]) + 1

  if not polynomial(coefs, n) == 0:
    n -= 1

  return n


#print(n, "=", res.real[abs(res.imag)<1e-5][-1])

def answer(s):
  if s == 1:
    return 4

  n = solve([1/3, 1/2, 1/6, -s])

  s -= n*(n+1)*(2*n+1)//6
  toothpicks = 2*n*(n+1)
  if s == 0:
    return toothpicks

  if s - 1 < triangle(n):
    s -= 1
    toothpicks += 3

    i = solve([1/2, 1/2, -s])

    toothpicks += i * 2

  else:
    s -= 2
    toothpicks += 6
    s -= triangle(n) - 1
    toothpicks += 2 * (n - 1)

    i = solve([1/2, 1/2, -s])

    toothpicks += i * 2

  return toothpicks


# iterative
def answer_iterative(s):
    for n in itertools.count():
        s -= n**2
        if s < 0:
            s += n**2
            break;

    toothpicks = 2*n*(n-1)
    if s == 0:
        return toothpicks

    s -= 1
    toothpicks += 3
    if s <= 0:
        return toothpicks

    for i in range(2, n):
        s -= i
        toothpicks += 2
        if s <= 0:
            return toothpicks

    s -= 1
    toothpicks += 3
    if s <= 0:
        return toothpicks

    for i in range(2, n + 1):
        s -= i
        toothpicks += 2
        if s <= 0:
            return toothpicks

    return toothpicks

def fast_answer(n):
  if n < 10000000:
    return answer_iterative(n)
  else:
    return answer(n)


# MAIN
if __name__ == "__main__":
    for _ in range(int(input())):
        print(answer_iterative(int(input())))
