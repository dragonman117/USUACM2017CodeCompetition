def gcf_iterations(n, m):
    if n < m:
        n, m = m, n

    itt = 0
    while not m == 0:
        itt += n // m
        n %= m
        n, m = m, n

    return itt

def answer(seeds, target):
    eucs_time = 2 # 2 months
    algs_time = 3 # 3 months

    eucs = target[1]
    algs = target[0]

    time = 0
    while True:
        if eucs < seeds[1] or algs < seeds[0]:
            return -1
        elif eucs == seeds[1] and algs == seeds[0]:
            return time
        elif eucs > algs:
            time += eucs // algs * algs_time
            eucs %= algs
        elif algs > eucs:
            time += algs // eucs * eucs_time
            algs %= eucs
        else:
            return -1
            # if eucs == algs and not the desired seed amount,
            #   then its impossible to get seeds > 0

def intput():
    return int(input())

if __name__ == "__main__":
    seeds = (intput(), intput());
    target = (intput(), intput());
    print(answer(seeds, target))
