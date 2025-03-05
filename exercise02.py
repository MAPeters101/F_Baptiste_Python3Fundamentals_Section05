"""
Exercise 2
Concatenate the following tuples into a single one, but replacing the odd value
s with zeros (0).

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
You can assume that every tuple is a sequence of consecutive integers starting
with an odd integer.

Try to write your code to be as generic as possible.
"""

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
# l = list(t1) +list(t2) + list(t3)
# for i in range(len(l)):
#     if l[i]%2 == 1:
#         l[i] = 0
# t = tuple(l)
# print(t)

l = list(t1) +list(t2) + list(t3)
l[::2] = [0] * len(l[::2])
t = tuple(l)
print(t)

