t = (1,2,3)
print(t, type(t))
print(t[0])
print(t[1])
print(t[-1])
print(len(t))
print(t[len(t)-1])
#t[2] = 40
print('-'*80)

t = ([1,2], [3,4])
print(t)
print(t[0], type(t[0]))
#t[0] = 100
l = t[0]
print(l)
l[0] = 100
print(l)
print(t)
t[1][1] = 400
print(t)
print('-'*80)

t = 1,2
print(t, type(t))

a = 10
b = 20
print((a, b, a+b))

t = a, b, a+b
print(t, type(t))
print('-'*80)

t = ()
print(t, type(t), len(t))

t = tuple()
print(t, type(t), len(t))
print('-'*80)

l = [1,2,3]
t = tuple(l)
print(l, type(l))
print(t, type(t))

print('-'*80)

t = 10, 20, 30
l = list(t)
print(t, type(t))
print(l, type(l))

print('-'*80)

t = 10, 20, 3, 40
print(t)
l = list(t)
l[2] = 30
print(l)
t = tuple(l)
print(t)

print('-'*80)
t = [1,2], 30, 40
print(t)
t[0][1] = 20
print(t)
l = list(t)
print(l)
print(l[0])
l[0][0] = 10
print(l)
print(t)






