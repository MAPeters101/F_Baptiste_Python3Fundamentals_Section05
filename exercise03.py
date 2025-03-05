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
"""
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(m[0])):
    m[i][i] = 1

print(m)
