def gcd_cross(n, m, target, iterations):
    x = (n - target) // m
    y = (n - target) / m

    if x == y:
        return iterations + x
    else:
        print(x, y)
        return -1

def answer(m, q, n, p):
    iterations = 0
    while n >= m and p >= q:
        if n > p:
            if p == q:
                return gcd_cross(n, p, m, iterations)
            iterations += n // p
            n %= p
        elif p > n:
            if n == m:
                return gcd_cross(p, n, q, iterations)
            iterations += p // n
            p %= n
        elif n == m and p == q:
            return iterations
        else:
            return -1
    return -1

def intput():
    return int(input())

if __name__ == "__main__":
    a = intput()
    e = intput()
    b = intput()
    f = intput()
    print(answer(a, e, b, f))

# def test(pods, target, expected):
#     result = answer(pods[0], pods[1], target[0], target[1])
#     if not result == expected:
#         print("Test Failed: expected=", expected, " but got=", result)
#
# test((3, 7), (3, 10), 1)
# test((3, 4), (3, 10), 2)
# test((3, 1), (3, 10), 3)
# test((2, 1), (3, 10), 4)
# test((1, 1), (3, 10), 5)
#
# test((2, 2), (3, 10), -1)
# test((2, 2), (3, 10), -1)
# test((2, 2), (10**10 - 1, 10**10), -1)
# test((2, 2), (4, 10), 3)
#
# raise TypeError


# OLD SOLUTION was a bit messier, new solution merges possible and gcd
# def gcd_will_cross(n, m, target):
#     return (n - target) / m == (n - target) // m
#
# def possible(a, e, b, f):
#     while b >= a and f >= e:
#         if b > f:
#             if f == e and gcd_will_cross(b, f, a):
#                 return True
#             b %= f
#         elif f > b:
#             if b == a and gcd_will_cross(f, b, e):
#                 return True
#             f %= b
#         else:
#             if b == a or f == e:
#                 return True
#             else:
#                 return False
#
#     return False
#
# def gcd(n, m):
#     if n < m:
#         n, m = m, n
#
#     it = -1
#     while not m == 0:
#         it += n // m
#         n %= m
#         n, m = m, n
#     return n, it
#
#
# def answer_old(a, e, b, f):
#     if not possible(a, e, b, f):
#         return -1
#     else:
#         pods = gcd(a, e)
#         target = gcd(b, f)
#
#         if pods[0] != target[0]:
#             return -1
#         else:
#             return target[1] - pods[1]
