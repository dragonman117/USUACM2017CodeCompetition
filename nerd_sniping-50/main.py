def solve():
    T = int(raw_input())

    A = [0] * T
    B = [0] * T
    K = [0] * T

    maxB = 0

    for idx in xrange(0, T):
        [A[idx], B[idx], K[idx]] = [int(x) for x in raw_input().split()]
        if B[idx] > maxB:
            maxB = B[idx]

    maxB += 1
    S = [0] * maxB

    for idx in xrange(2, maxB):
        if S[idx] == 0:
            for stride in xrange(idx, maxB, idx):
                S[stride] += 1

    for testNumber in xrange(0, T):
        count = 0
        k = K[testNumber]
        for idx in xrange(A[testNumber], B[testNumber] + 1):
            if S[idx] == k:
                count += 1
        print count

def main():
    solve()

if __name__ == "__main__":
    main()