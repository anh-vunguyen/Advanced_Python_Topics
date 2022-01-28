# itertools: product, permutation, combinations, accumulate ,groupby, and infinite iterators
# from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b) # cartesian product
# print(list(prod))
# prod = product(a, b, repeat=2) # cartesian product
# print(list(prod))

# permutation
# from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a)
# print(list(perm))
# perm = permutations(a, 2)
# print(list(perm))

# combinations
# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3]
# comb = combinations(a, 2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# accumulate
# from itertools import accumulate
# import operator
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))
# print("------")
# acc2 = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc2))
# print("------")
# acc2 = accumulate(a, func=max)
# print(a)
# print(list(acc2))

### groupby
# from itertools import groupby
#
# def smaller_than_3(x):
#     return x < 3
#
# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))
#
# # using lambda function
# group_obj = groupby(a, key=lambda x: x<3)
# for key, value in group_obj:
#     print(key, list(value))
#
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
# {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 26}]
# group_obj_2 = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj_2:
#     print(key, list(value))
# ###

### count, cycle, repeat
from itertools import count, cycle, repeat
# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)

a = [1, 2, 3]
for i in repeat(10, 4):
    print(i)
