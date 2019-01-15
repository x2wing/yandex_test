a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},  # a
    {c, e},  # b
    {d},  # c
    {e},  # d
    {f},  # e
    {c, g, h},  # f
    {f, h},  # g
    {f, g}  # h
]

VP = [False] * 8


def def1(v):
    if v == g:
        print('Congratulations you are in g')
    if not VP[v]:
        print('заход в вершину', v)
        VP[v] = True
        for i in N[v]:
            def1(i)
    else:
        print('не зашил в вершину', v)


if __name__ == '__main__':
    def1(0)
    print(sum(VP))

