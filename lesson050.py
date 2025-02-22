a = 'hello'
b = "Python"
a = "Python's best features:"
#a = 'Python's best features:'
a = 'Python\'s best features:'
print('-'*80)


s = 'Python rocks!'
print(s[0])
print(s[1])
print(s[len(s) - 1])
print(len(s))
print(s[-1])
print(s[-2])
print(s[0])
#s[0] = 'X'
a = ''
b = ""
print(type(a),len(a))
print(type(b),len(b))
print('-'*80)


s = str()
print(type(s),len(s))

t = (1, 2, 3)
print(t)
print(str(t))
s = str(t)
print(len(s))
print(s[0])
print()

s = 'Python'
t = tuple(s)
print(t, len(t))
l = list(s)
print(l, len(l))

