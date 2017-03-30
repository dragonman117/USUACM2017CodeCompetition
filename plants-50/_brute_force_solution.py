def answer(a, e, b, f, depth):
    if a == b and e == f:
        return depth
    elif a > b or e > f:
        return -1
    else:
        left = answer(a+e, e, b, f, depth + 1)
        right = answer(a, e+a, b, f, depth + 1)

        if left is not -1:
            return left
        else:
            return right

def intput():
    return int(input())

if __name__ == "__main__":
    for _ in range(int(input())):
        a, e, b, f = map(int, input().split())
        print(answer(a, e, b, f, 0))

