import numpy as np

na = np.array([1, 2, 3], dtype=np.str_)
# print(na)
# print(
# na.astype(np.string_)
# )


M = np.arange(1,25).reshape((6,4))
print(f'M={M}')
print(np.ix_([1,4], [3,0]))

R = np.random.randn(7)
print(R)