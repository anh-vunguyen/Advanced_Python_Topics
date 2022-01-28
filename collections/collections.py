# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# Counter
from collections import Counter
a = "aaaabbbcc" # iterable
my_counter = Counter(a) # returns a dictionary
print(my_counter)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

# namedtuple
# light weight object type
from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

# OrderedDict
from collections import OrderedDict
# it remembers the orders of items inserted
# since 3.7, it is not important anymore
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 9
print(ordered_dict)

# defaultdict
# # it has default value if the key has not been set yet.
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque
# double-ended queue
# add or remove elements from both ends
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
print(d.pop()) # return the last element
print(d.popleft()) # return the first element
d.extend([4, 5, 6])
print(d)
d.rotate(1) # rotate to the right
d.rotate(-1) # rotate to the left
print(d)
#d.clear()
