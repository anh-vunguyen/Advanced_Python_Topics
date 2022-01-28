import numpy as np

# Information about the knapsack, the constraints, etc.
# It should be noticed that each object is indivisible.
# If each object is divisible, we can use the Greedy algorithm to solve the problem
p = np.array([0, 1, 2, 5, 6])
wt = np.array([0, 2, 3, 4, 5])
m = 8
n = 4

# Finding the optimal profit value
k = np.zeros((n+1, m+1)) #(5, 9)
for i in range(n+1): # n is included
    for w in range(m+1): # m is included
        if (i == 0) or (w == 0):
            k[i, w] = 0
        elif (wt[i] <= w):
            k[i, w] = max(p[i] + k[i-1, int(w-wt[i])], k[i-1, w])
        else:
            k[i, w] = k[i-1, w]
print(f"The optimal value is {k[n, m]}")
print(k)

# Finding which objects are chosen in the optimal solution
i = n
j = m
object_selections = np.zeros((1, n+1))
while (i >= 0) and (j >= 0):
    if k[i, j] == k[i-1, j]:
        print(f"The object {i} is NOT selected.")
        i -= 1
    else:
        print(f"The object {i} is selected.")
        object_selections[0, i] = 1
        j -= wt[i]
        i -= 1 # Decrementation after we substract the weight of object i
print('-'*20)
print(object_selections)
