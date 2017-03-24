import _brute_force_solution
import _iterative_solution
import solution

# print("")
# print(_brute_force_solution.answer(1, 1, 10000, 10001, 0)) # brute force fails to exceed 10^4
# print("")
#
# raise TypeError


# print("")
# print(_iterative_solution.answer(1, 1, 10**8-2, 10**8-1)) # iterative solution fails to exceed 10^8
# print("")
#
# raise TypeError

def gcd(n, m):
    if n < m:
        n, m = m, n
    count = -1
    while m != 0:
        print(n, m)
        count += n // m
        n %= m
        n, m = m, n
    return count, n

gcd(19*2*3*5*5*2, 2*2*7*12*2*2*2*2*2)

# x = 10**15
# y = 10**15+1
#
# for i in range(1000000):
#     g = gcd(x - i, y - i)[0]
#     me = solution.answer(1, 1, x - i, y - i)
#
#     if me != g:
#         print(i, g, me)
#         raise TypeError

def test(a, b, c, d):
    expected = gcd(c, d)[0] - gcd(a, b)[0]
    result = solution.answer(a, b, c, d)
    if result != expected:
        print(a, b, c, d, "Test failed: expected", expected, " but got=", result)

# test(1, 1, 920419823, 433024223) # big primes
# test(1, 1, 920419823, 433024223**2) # big primes
# test(1, 1, 920419823**2, 433024223) # big primes
# test(1, 1, 920419823**2, 433024223**2) # big primes
# test(3, 1, 433024223**2, 920419823) # big primes
# test(1, 1, 433024223**2, 920419823**2) # big primes
# test(3905207, 3192530, 433024223**2, 920419823**2) # big primes
# a, b = 3905207-91, 3192530-91
# test(10000, 10000, a*10000, b*10000)
# test(1000, 1000, 433024223*1000, 920419823*1000) # big primes

# takes roughly 8 seconds
# for a in range(1, 20):
#     for e in range(1, 20):
#         for b in range(a, 50):
#             for f in range(e, 50):
#                 brute = _brute_force_solution.answer(a, e, b, f, 0)
#                 iterative = _iterative_solution.answer(a, e, b, f)
#                 answer = solution.answer(a, e, b, f)
#                 if brute != answer:
#                     print(a, e, b, f, "Failed:  expected=", brute, " but got=", answer)
#                 if brute != iterative:
#                     print(a, e, b, f, "Failed:  expected=", brute, " but iterative=", iterative)
