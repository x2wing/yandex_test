import operator
import functools

n = 5
m = 2
functools.reduce(lambda x, y: x * y, range(1, n), 2)

matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]
import itertools

# ****************list flattening**********************************
flattened = itertools.chain.from_iterable(matrix)
# ****************list flattening**********************************

# print(*flattened)


a = [[0, 1, 2, 3],[10, 11, 12, 13],[20, 21, 22, 23]]
print(
sum(a, [1,2,3,4])
)