import random

a = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 10)
print(c)

d = random.randrange(1, 10)
print(d)

# Normal Distribution
e = random.normalvariate(0, 1)
print(e)

mylist = list("ABCDEFGH")
print(mylist)
f = random.choice(mylist)
print(f)

g = random.sample(mylist, 3) # Sampling without replacement
print(g)

h = random.choices(mylist, k=3) # Sampling with replacement
print(h)

random.shuffle(mylist)
print(mylist)

# Pseudo-random | Reproducable
random.seed(42)
print(random.random())
print(random.randint(1, 10))
# Reseed
random.seed(42)
print(random.random())
print(random.randint(1, 10))

print('-'*10 + 'secrets module' + '-'*10)
# Secrets modules - Used for passwords, security tokens, account authentication
import secrets
a = secrets.randbelow(10) # Exclusive upperbound
print(a) # Truly random

b = secrets.randbits(4) # returns k random bits
print(b)

mylist = list("SECRET")
c = secrets.choice(mylist)
print(c)

print('-'*10 + 'numpy module' + '-'*10)
import numpy as np
a = np.random.rand(3)
print(a) # 1-D array with 3 elements

a = np.random.rand(3, 3)
print(a) # 2-D array | Matrix 3x3

a = np.random.randint(0, 10, 3)
print(a)

a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr) # Shuffle along the first axis
print(arr)

np.random.seed(42)
print(np.random.rand(3,3))
np.random.seed(42)
print(np.random.rand(3,3))
