def gcd_cross(n, m, target, iterations):
    if n == target:
        return iterations
    while n > m:
        iterations += 1
        n -= m
        if n == target:
            return iterations
    return -1

def answer(m, q, n, p):
    iterations = 0
    while n >= m and p >= q:
        if n > p:
            if p == q:
                return gcd_cross(n, p, m, iterations)
            iterations += 1
            n -= p
        elif p > n:
            if n == m:
                return gcd_cross(p, n, q, iterations)
            iterations += 1
            p -= n
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
