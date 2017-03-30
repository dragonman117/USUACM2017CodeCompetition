def gcd_cross(n, m, target, iterations):
    if (n - target) % m == 0:
        return iterations + (n - target) // m
    else:
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
    for _ in range(int(input())):
        a, e, b, f = map(int, input().split())
        print(answer(a, e, b, f))

