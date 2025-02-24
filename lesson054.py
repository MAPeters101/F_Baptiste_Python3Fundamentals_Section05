l = [10, 20, 3, 40, 50]
print(l)
l[2] = 30
print(l)
print()
l = [1, 20, 30, 5, 6]
print(l)
print(l[1:3])
l[1:3] = (2,3,4)
print(l)
print()
print(l[1:3])
l[1:3] = 'python'
print(l)
print("-"*80)

l = [1,2,3,4,5,6,7,8]
print(l[1::2])
l[1::2] = 20, 40, 60, 80
print(l)
#l[1::2] = 20, 40, 60
#l[1::2] = 20, 40, 60, 80, 100
print(l)
print('-'*80)

l = [1,2,3,4,5,6,7,8]
print(l[:-3:-1])
l[:-3:-1] = 100, 200
print(l)
print('-'*80)

l = [1,2,3,4,5,6,7,8]
print(l[1:4])
l[1:4] = 10, 20
print(l)
del l[2]
print(l)
print()

l = [1,2,3,4,5,6]
print(l[::2])
del l[::2]
print(l)
print('-'*80)


l = [1,2,3,4]
print(l)
l.append(5)
print(l)
l.append('python')
print(l)
l.append((1,2,3))
print(l)
print()

l = [1,2,3,4]
print(l)
l.extend([5,6,7,8])
print(l)
l.extend((10,20))
print(l)
l.extend('python')
print(l)
print()

l = [1,2,3,4]
print(l)
print(l[2])
l.insert(2, 'a')
print(l)
l.insert(0, 'abc')
print(l)
print('-'*80)

from timeit import timeit
l = []
print(timeit('l.append(1)',globals=globals(), number=100_000))
print(len(l))
print()

l = []
print(timeit('l.insert(0,1)',globals=globals(), number=100_000))
print(len(l))
print()






