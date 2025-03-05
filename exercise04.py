"""
Exercise 3
Given the following matrix:

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Make this matrix into an identity matrix (setting the diagonal elements to 1).

Your code should mutate m.

Exercise 4
Do the same problem as Exercise 3, but do not mutate m.
"""
import copy

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

n = copy.deepcopy(m)
for i in range(len(n[0])):
    n[i][i] = 1
print(m)
print(n)

