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





