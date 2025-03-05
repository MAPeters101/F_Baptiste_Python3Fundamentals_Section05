"""
Exercise 1
Given the following string:

s = 'FfEeDdCcBbAa'
Create two new variables that contain just the lower and upper case letters of
s respectively, in the correct alphabetical order, i.e:

'ABCDEF'
'abcdef'
"""

s = 'FfEeDdCcBbAa'
# ll = []
# ul = []
# for char in s:
#     if char.isupper():
#         ul.append(char)
#     else:
#         ll.append(char)
# ll.sort()
# ul.sort()
# l = ''.join(ll)
# u = ''.join(ul)
# print(u)
# print(l)
rev_s = s[::-1]
ll = rev_s[::2]
ul = rev_s[1::2]
print(ll)
print(ul)

