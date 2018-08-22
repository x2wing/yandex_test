from random import randint as ri

M = list(range(10))


def banerokrutilka(M):
    n = len(M) - 1
    result = []
    while M:
        result += [M.pop(ri(0, n))]
        n -= 1
    return result


banerokrutilka2 = lambda M: [M.pop(ri(0, i - 1)) for i in range(len(M), 0, -1)]


def checker(before, after):
    # print('before = ', before, 'after = ', after)
    # print(len(before) == len(after))
    # print(set(before) == set(after))
    # print(before != after)
    if len(before) == len(after) \
            and set(before) == set(after) \
            and before != after:
        return "passed"


if __name__ == '__main__':
    # banerokrutilka2(M)
    print(
        checker(M.copy(), banerokrutilka2(M))
    )
