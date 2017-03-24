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
    pods = (intput(), intput());
    target = (intput(), intput());
    print(answer(pods[0], pods[1], target[0], target[1], 0))

# def brute_test(pods, target, expected):
#     result = answer(pods[0], pods[1], target[0], target[1], 0)
#     if not result == expected:
#         print("Test Failed: expected=", expected, " but got=", result)
#
# brute_test((1, 1), (3, 10), 5)
# brute_test((2, 2), (3, 10), -1)
# brute_test((2, 2), (3, 10), -1)
# # brute_test((2, 2), (10**10 - 1, 10**10), -1)
# brute_test((2, 2), (4, 10), 3)
