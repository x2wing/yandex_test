list_c = [t + t ** 2 for t in (2 * x ** 3 + 5 * x ** 4 for x in range(-2, 4))]
list_d = [2 * x ** 3 + 5 * x ** 4 + x+ x**2 for x in range(-2, 4)]
print(list_c)
print(list_d)
