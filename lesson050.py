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
print('-'*80)

l = ['a', 'b', 'c', 'd', 'e', 'f']
print(l)
l = ['abcdef']
print(l)
l = list('abcdef')
print(l)

s='===================='
print(len(s))

s = '=//=' * 10
print(s)

t = (1,2,3) * 3
print(t)

l = [1,2,3] * 3
print(l)
print('-'*80)

l = [0] * 10
print(l)

t = ([1,2], 30)
t2 = t * 3
print(t2)
print(t2[0] is t[0])
print(t2[2] is t[0])
print(t2[4] is t[0])
print(t2[2] is t2[0])

print()
m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(m[0][0], m[0][1], m[2][2])

row_1 = m[0]
print(row_1)
print(row_1[1])
row_1[0] = 1
print(m)
m[1][1] = 1
m[2][2] = 1
print(m)

print('='*80)

m = [[0,0,0]] * 3
print(m)
print(m[0] is m[1])
m[0][0] = 1
print(m)

row = [0,0,0]
m = [row] * 3
print(m)
