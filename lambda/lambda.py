# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

# multiple arguments
mult = lambda x, y: x * y
print(mult(10, 9))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) # sorted by x
print(points2D)
print(points2D_sorted)
points2D_ysorted = sorted(points2D, key=lambda x: x[1]) # sorted by y
print(points2D)
print(points2D_ysorted)
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) # sorted by y
print(points2D)
print(points2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(a)
print(list(b))
c = [2*x for x in a] # list comprehesion
print(list(c))

# filter function
# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b))
print([x for x in a if x % 2==0])

# reduce function
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
